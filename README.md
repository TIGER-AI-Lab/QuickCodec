QuickCodec
====

QuickCodec is designed for fast loading videos for VLLMs, especially long videos with relatively high frame sampling rates.

---

![version]


Installation
------------

The easiest way to use QuickCodec is via the binary wheels are provided on [PyPI][pypi] for Linux, MacOS and Windows linked against the latest stable version of ffmpeg. You can install these wheels by running:

```bash
pip install quickcodec
```


Installing From Source
----------------------

For the more adventurous fold  Here's how to build PyAV from source. You must use [MSYS2](https://www.msys2.org/) when using Windows.

```bash
git clone https://github.com/PyAV-Org/PyAV.git
cd PyAV
source scripts/activate.sh

# Build ffmpeg from source. You can skip this step
# if ffmpeg is already installed.
./scripts/build-deps

# Build PyAV
./scripts/build

# if you want to install it globally instead of in the env, deactivate
deactivate

pip install .
```

---

Roadmap
----------------------

QuickCodec is ojnly just getting started!
As our lab is always working on (long) video, we will continue to add new features and remove sharp edges.

- Pull in qwen_procesing to this library, as it is the last bottleneck after accelerating prefill and loading.
- Support more sparse access patterns, I.e. a seek-if-needed design.
- Add more elegant handling of shared memory.
- Add long lived workers.
- Add better error handling if a subprocess blows up.


Supported Platforms
----------------------
- **Linux:** this is our main platform and what we test against. If you have problems with any linux distro please open an issue and we will try to resolve it.
- **MacOS:** as it is unix-like, everything should work for MacOS, however *we do not actively test against it*.
- **Windows:** we build for it, however it is quite different and you may encounter weird problems.

Notice
----------------------
QuickVideo is build on top of [FFmpeg][ffmpeg] and [PyAv][pyav] libraries.  
Huge thanks to the contributors and maintainers of those libraries, they have done a huge amount of work create a clean interface that handles a lot of the messy nature of multimedia processing.
This project is **not endorsed** any maintainer of PyAv or FFmpeg, if you have any problems with QuickCodec please open as issue on **this repository**.
We inherit all the features of PyAv (including processing for other modalities like audio) which you can read about [here][docs], have fun!


[conda-badge]: https://img.shields.io/conda/vn/conda-forge/av.svg?colorB=CCB39A
[conda]: https://anaconda.org/conda-forge/av
[docs-badge]: https://img.shields.io/badge/docs-on%20pyav.basswood--io.com-blue.svg
[docs]: https://pyav.basswood-io.com
[pypi-badge]: https://img.shields.io/pypi/v/av.svg?colorB=CCB39A
[pypi]: https://pypi.org/project/quickvideo
[discuss]: https://github.com/PyAV-Org/PyAV/discussions
[version]: https://img.shields.io/badge/Version-0.0.1-blue
[github-tests-badge]: https://github.com/PyAV-Org/PyAV/workflows/tests/badge.svg
[github-tests]: https://github.com/PyAV-Org/PyAV/actions?workflow=tests
[github]: https://github.com/TigerLab/PyAV

[ffmpeg]: https://ffmpeg.org/
[pyav]: https://github.com/PyAV-Org/PyAV
