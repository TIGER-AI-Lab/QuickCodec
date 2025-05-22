from quickcodec.packet import Packet
from quickcodec.stream import Stream
from quickcodec.subtitles.subtitle import SubtitleSet

class SubtitleStream(Stream):
    def decode(self, packet: Packet | None = None) -> list[SubtitleSet]: ...
