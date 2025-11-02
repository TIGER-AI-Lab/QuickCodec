import torch
from torchcodec.decoders import VideoDecoder
from time import perf_counter_ns
import argparse

def bench(f, *args, num_exp=3, warmup=1, **kwargs):
    """Benchmark a function by running it multiple times and measuring execution time."""
    print(f"Executing warmup runs: {warmup}")
    for _ in range(warmup):
        f(*args, **kwargs)


    print(f"Executing timing experiments with runs: {num_exp}")
    times = []
    for _ in range(num_exp):
        start = perf_counter_ns()
        result = f(*args, **kwargs)
        end = perf_counter_ns()
        times.append(end - start)

    return torch.tensor(times).float(), result


def report_stats(times, unit="s"):
    """Report median and standard deviation of benchmark times."""
    mul = {
        "ns": 1,
        "µs": 1e-3,
        "ms": 1e-6,
        "s": 1e-9,
    }[unit]
    times = times * mul
    std = times.std().item()
    med = times.median().item()
    print(f"median = {med:.2f}{unit} ± {std:.2f}")
    return med


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark video reading performance.")
    parser.add_argument("video_path", type=str, help="Path to the input video file")
    parser.add_argument("--threads", type=int, default=16, help="Number of threads to use")
    parser.add_argument("--device", type=str, default="cpu", help="Device to use for decoding")
    args = parser.parse_args()
    (video_path, threads, device) = args.video_path, args.threads, args.device

    vr = VideoDecoder(video_path, device="cuda")

    meta = vr.metadata
    fps = round(meta.average_fps)
    num_frames = meta.num_frames
    duration = num_frames / fps

    print(f"Framerate: {fps:.2f} fps")
    print(f"Total frames: {num_frames}")
    print(f"Duration: {duration:.2f} seconds")

    sample_indices = [int(i * fps) for i in range(int(duration)) if i * fps < num_frames]
    print(f"Sampling {len(sample_indices)} frames (1 per second)")
        
    times, result_sequential = bench(vr.get_frames_at, sample_indices)
    sequential_time = report_stats(times, unit="s")


