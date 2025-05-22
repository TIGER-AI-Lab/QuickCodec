import time
import traceback
import numpy as np


video_path = "/home/bsch/20min.mp4"
height = 360
width = 224
threads = [2,4,8]

results = []


from quickcodec import VideoReader, InterleavedVideoReader

vr = VideoReader(video_path, num_threads=threads[1])
indices = list(range(0,len(vr), 2))
front_load = vr.get_batch(indices)

#print(f"control batch has shape: {b.shape}")



thread = threads[2]

vr2 = InterleavedVideoReader(video_path, num_threads=thread, num_intervals=16)
vr2.process(indices)
vr2.frame_iter = 16
idx = 0

for it, data in enumerate(iter(vr2)):
    
    global_end = vr2.frames_shape[0]
    end = idx + vr2.frame_iter
    if global_end < end: end = global_end
    
    assert np.array_equal(front_load[idx:end], data), f"assert failed on {it}"

    idx += vr2.frame_iter

assert vr2.all_loaded, "all frames have not been loaded"

print("DONE")