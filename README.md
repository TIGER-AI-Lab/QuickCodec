QuickCodec
====

QuickCodec is designed for fast loading videos for VLLMs, especially long videos with relatively high frame sampling rates.

---

[![GitHub Test Status][github-tests-badge]][github-tests] [![Documentation][docs-badge]][docs] [![Python Package Index][pypi-badge]][pypi]


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
[pypi]: https://pypi.org/project/av
[discuss]: https://github.com/PyAV-Org/PyAV/discussions

[github-tests-badge]: https://github.com/PyAV-Org/PyAV/workflows/tests/badge.svg
[github-tests]: https://github.com/PyAV-Org/PyAV/actions?workflow=tests
[github]: https://github.com/TigerLab/PyAV

[ffmpeg]: https://ffmpeg.org/
[conda-forge]: https://conda-forge.github.io/
[conda-install]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
[pyav]: https://github.com/PyAV-Org/PyAV
