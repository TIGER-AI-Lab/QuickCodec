cimport libav as lib

from quickcodec.codec.context cimport CodecContext
from quickcodec.container.core cimport Container
from quickcodec.frame cimport Frame
from quickcodec.packet cimport Packet


cdef class Stream:
    cdef lib.AVStream *ptr

    # Stream attributes.
    cdef readonly Container container
    cdef readonly dict metadata

    # CodecContext attributes.
    cdef readonly CodecContext codec_context

    # Private API.
    cdef _init(self, Container, lib.AVStream*, CodecContext)
    cdef _finalize_for_output(self)
    cdef _set_time_base(self, value)
    cdef _set_id(self, value)


cdef Stream wrap_stream(Container, lib.AVStream*, CodecContext)
