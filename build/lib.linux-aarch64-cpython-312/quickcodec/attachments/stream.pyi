from typing import Literal

from quickcodec.stream import Stream

class AttachmentStream(Stream):
    type: Literal["attachment"]
    @property
    def mimetype(self) -> str | None: ...
