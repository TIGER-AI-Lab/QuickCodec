video_path = "/home/bsch/60min.mp4"
thread = 4
from quickcodec import VideoReader


vr = VideoReader(video_path, num_threads=thread)

print(f"Num frames is {len(vr)}")
print(f"Height is {vr.height}")
print(f"Width is {vr.width}")
print(f"FPS is {vr.get_fps()}")