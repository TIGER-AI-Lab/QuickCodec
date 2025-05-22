from quickcodec.vfast import vfast_load, get_stats
import numpy as np
import time

def main(video_path):

    video_path = str(video_path)
    d = get_stats(video_path)

    indices = list(range(0,91500, 25))

    for thread in [8,4]:
        s = time.time()
        data = vfast_load(video_path, indices=indices, height=360, width=360, num_threads=thread)
        e = time.time()
        print(f"Timing was: {e-s}")

    

if __name__ == "__main__":
    from pathlib import Path

    home_dir = Path.home()
    mp4_files = home_dir.rglob("*.mp4")  # Recursively search for .mp4 files
    file = next(mp4_files)
    
    print(f"Testing {file}")
    main(file)