import quickcodec
import time
from quickcodec.vfast import estimate_frame_location
def main(test_video):

    # s = time.time()
    out = quickcodec.get_stats(test_video)
    # e = time.time()
    container = quickcodec.open(test_video)

    fails = []
    for real_loc, frame in enumerate(container.decode(video=0)):
        
        
        pts = frame.pts

        est_loc = estimate_frame_location(pts, out['start'], out['end'], out['num_frames'])
        if (not (est_loc == real_loc)):
            print(f"Was off by {est_loc-real_loc} correct was {real_loc} estimated was {-1} after rnd it was {est_loc}")
            fails.append(1)

            

    print(f"total number of fails was: {len(fails)} out of {out["num_frames"]}")

# print(out)
# print(f"Timed was {e-s} seconds")

if __name__ == "__main__":
    from pathlib import Path

    home_dir = Path.home()
    mp4_files = home_dir.rglob("*.mp4")  # Recursively search for .mp4 files

    for file in mp4_files:
        print(f"Testing {file}")
        main(file)