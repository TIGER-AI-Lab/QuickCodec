from quickcodec.packet cimport Packet
from quickcodec.stream cimport Stream


cdef class SubtitleStream(Stream):
    cpdef decode(self, Packet packet=?)
