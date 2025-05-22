from quickcodec.packet cimport Packet
from quickcodec.stream cimport Stream

from .frame cimport VideoFrame


cdef class VideoStream(Stream):
    cpdef encode(self, VideoFrame frame=?)
    cpdef decode(self, Packet packet=?)
