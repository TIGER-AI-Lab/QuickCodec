from __future__ import annotations

import argparse
import base64
import pickle
from multiprocessing import resource_tracker

def remove_shm_from_resource_tracker():
    """
    Monkey-patch multiprocessing.resource_tracker so SharedMemory won't be tracked.
    Prevents the resource tracker from freeing our shared memory on process exit.
    That responsibility is left to the process that created the shared memory.
    Which you would expect as the default behaviour but python's parellel processing libraries suck
    More details at:
    https://stackoverflow.com/questions/77285558/why-does-python-shared-memory-implicitly-unlinked-on-exit
    https://bugs.python.org/issue38119

    python 3.13 adds the more elegant "track" flag on SharedMemory
    see:
    https://github.com/python/cpython/pull/21516
    https://docs.python.org/3.13/library/multiprocessing.shared_memory.html

    Can switch to that when people update to python 3.13 in 2070.
    """

    def fix_register(name, rtype):
        if rtype == "shared_memory":
            return
        return resource_tracker._resource_tracker.register(name, rtype)
    resource_tracker.register = fix_register

    def fix_unregister(name, rtype):
        if rtype == "shared_memory":
            return
        return resource_tracker._resource_tracker.unregister(name, rtype)
    resource_tracker.unregister = fix_unregister

    if "shared_memory" in resource_tracker._CLEANUP_FUNCS:
        del resource_tracker._CLEANUP_FUNCS["shared_memory"]

def mp_entrypoint():
    import sys
    remove_shm_from_resource_tracker()
    from quickcodec.container import parallel_open
    # Parse args
    filename = sys.argv[1]
    shm_buf_con = sys.argv[2]
    frames_to_save = sys.argv[3]
    interval_min_pts = int(sys.argv[4])
    interval_max_pts = int(sys.argv[5])
    height = int(sys.argv[6])
    width = int(sys.argv[7])
    num_frames = int(sys.argv[8])
    rank = int(sys.argv[9])
    world_size = int(sys.argv[10])
    global_min_pts = int(sys.argv[11])
    global_max_pts = int(sys.argv[12])
    interpolation  = sys.argv[13]

    pickled = base64.b64decode(frames_to_save.encode('utf-8'))
    frames_to_save = pickle.loads(pickled)
    # print(filename)
    # print(shm_buf_con)
    # print(frames_to_save)
    # print(interval_min_pts)
    # print(interval_max_pts)
    # print(buffer_size)
    # print(height)
    # print(width)
    # print(num_frames)
    # print(rank)
    # print(world_size)
    # print(global_min_pts)
    # print(global_max_pts)
    parallel_open(
        filename,
        shm_buf_con,
        frames_to_save,
        interval_min_pts,
        interval_max_pts,
        height,
        width,
        num_frames,
        rank,
        world_size,
        global_min_pts,
        global_max_pts,
        interpolation
    )

def mp_interleaved_entrypoint():
    import sys
    remove_shm_from_resource_tracker()
    from quickcodec.container import interleaved_parallel_open

    # Parse args
    filename = sys.argv[1]
    shm_buf_con = sys.argv[2]
    frames_to_save = sys.argv[3]
    interval_list_of_lists = sys.argv[4]
    height = int(sys.argv[5])
    width = int(sys.argv[6])
    num_frames = int(sys.argv[7])
    rank = int(sys.argv[8])
    world_size = int(sys.argv[9])
    global_min_pts = int(sys.argv[10])
    global_max_pts = int(sys.argv[11])
    interpolation  = sys.argv[12]
    shm_check_buf  = sys.argv[13]

    pickled = base64.b64decode(frames_to_save.encode('utf-8'))
    frames_to_save = pickle.loads(pickled)
    
    interval_list_of_lists = base64.b64decode(interval_list_of_lists.encode('utf-8'))
    interval_list_of_lists = pickle.loads(interval_list_of_lists)

    interleaved_parallel_open(
        filename,
        shm_buf_con,
        frames_to_save,
        0,
        0,
        height,
        width,
        num_frames,
        rank,
        world_size,
        global_min_pts,
        global_max_pts,
        interpolation,
        shm_check_buf,
        interval_list_of_lists[rank]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codecs", action="store_true")
    parser.add_argument("--hwdevices", action="store_true")
    parser.add_argument("--hwconfigs", action="store_true")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args()

    if args.version:
        import quickcodec
        import quickcodec._core

        print(f"PyAV v{quickcodec.__version__}")

        by_config: dict = {}
        for libname, config in sorted(quickcodec._core.library_meta.items()):
            version = config["version"]
            if version[0] >= 0:
                by_config.setdefault(
                    (config["configuration"], config["license"]), []
                ).append((libname, config))

        for (config, license), libs in sorted(by_config.items()):
            print("library configuration:", config)
            print("library license:", license)
            for libname, config in libs:
                version = config["version"]
                print(f"{libname:<13} {version[0]:3d}.{version[1]:3d}.{version[2]:3d}")

    if args.hwdevices:
        from quickcodec.codec.hwaccel import hwdevices_available

        print("Hardware device types:")
        for x in hwdevices_available():
            print("   ", x)

    if args.hwconfigs:
        from quickcodec.codec.codec import dump_hwconfigs

        dump_hwconfigs()

    if args.codecs:
        from quickcodec.codec.codec import dump_codecs

        dump_codecs()


if __name__ == "__main__":
    main()
