import time
import traceback
import multiprocessing.shared_memory
from multiprocessing.resource_tracker import _resource_tracker
import numpy as np


video_path = "/home/bsch/20min.mp4"
height = 360
width = 224
max_num_threads = [1,2,4,8,16]

results = []

for thread in max_num_threads:
        from quickcodec import VideoReader
        vr = VideoReader(video_path, num_threads=thread)
        indices = list(range(0,len(vr), 25))
        s = time.time()
        b = vr.get_batch(indices)
        results.append(b)
        e = time.time()
        print(b)
        print(f"quickcodec took {e-s} with {thread} threads")
        print(b.shape)
            
baseline = results[0]

for idx, ele in enumerate(results):
    print(f"{idx}: {np.array_equal(baseline, ele)}")