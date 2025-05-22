from typing import Literal

from quickcodec.codec.context import CodecContext

class SubtitleCodecContext(CodecContext):
    type: Literal["subtitle"]
