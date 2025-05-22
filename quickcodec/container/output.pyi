from fractions import Fraction
from typing import Sequence, TypeVar, Union, overload

from quickcodec.audio import _AudioCodecName
from quickcodec.audio.stream import AudioStream
from quickcodec.data.stream import DataStream
from quickcodec.packet import Packet
from quickcodec.subtitles.stream import SubtitleStream
from quickcodec.video import _VideoCodecName
from quickcodec.video.stream import VideoStream

from .core import Container

_StreamT = TypeVar("_StreamT", bound=Union[VideoStream, AudioStream, SubtitleStream])

class OutputContainer(Container):
    def __enter__(self) -> OutputContainer: ...
    @overload
    def add_stream(
        self,
        codec_name: _AudioCodecName,
        rate: int | None = None,
        options: dict[str, str] | None = None,
        **kwargs,
    ) -> AudioStream: ...
    @overload
    def add_stream(
        self,
        codec_name: _VideoCodecName,
        rate: Fraction | int | None = None,
        options: dict[str, str] | None = None,
        **kwargs,
    ) -> VideoStream: ...
    @overload
    def add_stream(
        self,
        codec_name: str,
        rate: Fraction | int | None = None,
        options: dict[str, str] | None = None,
        **kwargs,
    ) -> VideoStream | AudioStream | SubtitleStream: ...
    def add_stream_from_template(
        self, template: _StreamT, opaque: bool | None = None, **kwargs
    ) -> _StreamT: ...
    def add_data_stream(
        self, codec_name: str | None = None, options: dict[str, str] | None = None
    ) -> DataStream: ...
    def start_encoding(self) -> None: ...
    def close(self) -> None: ...
    def mux(self, packets: Packet | Sequence[Packet]) -> None: ...
    def mux_one(self, packet: Packet) -> None: ...
    @property
    def default_video_codec(self) -> str: ...
    @property
    def default_audio_codec(self) -> str: ...
    @property
    def default_subtitle_codec(self) -> str: ...
    @property
    def supported_codecs(self) -> set[str]: ...
