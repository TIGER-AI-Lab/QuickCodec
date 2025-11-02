"""
Adapted from torch codec:
https://meta-pytorch.org/torchcodec/stable/generated_examples/decoding/parallel_decoding.html
"""

import torch
from typing import List
from joblib import Parallel, delayed
from torchcodec.decoders import VideoDecoder
import numpy as np

class VideoReader:

    def __init__(self, video_path, device="cpu", parrallel=8):

        self.video_path = video_path
        self.device = device
        self.parrallel = parrallel
        self.decoder = VideoDecoder(video_path, seek_mode="approximate", device="cpu")
        self.metadata = self.decoder.metadata

    def get_frames_at(self, indices: List[int])->torch.Tensor:
        self.decode_with_multithreading(indices, self.video_path)

    def __len__(self):
        return len(self.decoder)

    def split_indices(self, indices: List[int], num_chunks: int) -> List[List[int]]:
        """Split a list of indices into approximately equal chunks."""
        chunk_size = len(indices) // num_chunks
        chunks = []

        for i in range(num_chunks - 1):
            chunks.append(indices[i * chunk_size:(i + 1) * chunk_size])

        chunks.append(indices[(num_chunks - 1) * chunk_size:])
        return chunks

    def decode_sequentially(self, indices: List[int], video_path=None):
        """Decode frames sequentially using a single decoder instance."""
        decoder = VideoDecoder(video_path, seek_mode="approximate", device=self.device)
        return decoder.get_frames_at(indices)

    def decode_with_multithreading(
        self,
        indices: List[int],
        video_path: str,
    ):
        """Decode frames using multiple threads with joblib."""
        chunks = self.split_indices(indices, num_chunks=self.parrallel)

        results = Parallel(n_jobs=self.parrallel, prefer="threads", verbose=0)(
            delayed(self.decode_sequentially)(chunk, video_path) for chunk in chunks
        )

        return torch.cat([frame_batch.data for frame_batch in results], dim=0)