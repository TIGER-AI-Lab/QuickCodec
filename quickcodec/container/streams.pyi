from typing import Iterator, Literal, overload

from quickcodec.attachments.stream import AttachmentStream
from quickcodec.audio.stream import AudioStream
from quickcodec.data.stream import DataStream
from quickcodec.stream import Stream
from quickcodec.subtitles.stream import SubtitleStream
from quickcodec.video.stream import VideoStream

class StreamContainer:
    video: tuple[VideoStream, ...]
    audio: tuple[AudioStream, ...]
    subtitles: tuple[SubtitleStream, ...]
    attachments: tuple[AttachmentStream, ...]
    data: tuple[DataStream, ...]
    other: tuple[Stream, ...]

    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Stream]: ...
    @overload
    def __getitem__(self, index: int) -> Stream: ...
    @overload
    def __getitem__(self, index: slice) -> list[Stream]: ...
    @overload
    def __getitem__(self, index: int | slice) -> Stream | list[Stream]: ...
    def get(
        self,
        *args: int | Stream | dict[str, int | tuple[int, ...]],
        **kwargs: int | tuple[int, ...],
    ) -> list[Stream]: ...
    def best(
        self,
        type: Literal["video", "audio", "subtitle", "data", "attachment"],
        /,
        related: Stream | None = None,
    ) -> Stream | None: ...
