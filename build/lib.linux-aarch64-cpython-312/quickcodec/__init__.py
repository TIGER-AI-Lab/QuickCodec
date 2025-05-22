# MUST import the core before anything else in order to initialize the underlying
# library that is being wrapped.
from quickcodec._core import time_base, library_versions, ffmpeg_version_info

# Capture logging (by importing it).
from quickcodec import logging

# For convenience, import all common attributes.
from quickcodec.about import __version__
from quickcodec.audio.codeccontext import AudioCodecContext
from quickcodec.audio.fifo import AudioFifo
from quickcodec.audio.format import AudioFormat
from quickcodec.audio.frame import AudioFrame
from quickcodec.audio.layout import AudioLayout
from quickcodec.audio.resampler import AudioResampler
from quickcodec.audio.stream import AudioStream
from quickcodec.bitstream import BitStreamFilterContext, bitstream_filters_available
from quickcodec.codec.codec import Codec, codecs_available
from quickcodec.codec.context import CodecContext
from quickcodec.codec.hwaccel import HWConfig
from quickcodec.container import open
from quickcodec.format import ContainerFormat, formats_available
from quickcodec.packet import Packet
from quickcodec.error import *  # noqa: F403; This is limited to exception types.
from quickcodec.video.codeccontext import VideoCodecContext
from quickcodec.video.format import VideoFormat
from quickcodec.video.frame import VideoFrame
from quickcodec.video.stream import VideoStream
from quickcodec.vfast import VideoReader, InterleavedVideoReader


__all__ = (
    "__version__",
    "time_base",
    "ffmpeg_version_info",
    "library_versions",
    "AudioCodecContext",
    "AudioFifo",
    "AudioFormat",
    "AudioFrame",
    "AudioLayout",
    "AudioResampler",
    "AudioStream",
    "BitStreamFilterContext",
    "bitstream_filters_available",
    "Codec",
    "codecs_available",
    "CodecContext",
    "open",
    "ContainerFormat",
    "formats_available",
    "Packet",
    "VideoCodecContext",
    "VideoFormat",
    "VideoFrame",
    "VideoStream",
    "VideoReader"
    "InterleavedVideoReader"
)


def get_include() -> str:
    """
    Returns the path to the `include` folder to be used when building extensions to av.
    """
    import os

    # Installed package
    include_path = os.path.join(os.path.dirname(__file__), "include")
    if os.path.exists(include_path):
        return include_path
    # Running from source directory
    return os.path.join(os.path.dirname(__file__), os.pardir, "include")
