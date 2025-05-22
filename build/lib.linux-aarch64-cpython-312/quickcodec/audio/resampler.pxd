from quickcodec.audio.format cimport AudioFormat
from quickcodec.audio.frame cimport AudioFrame
from quickcodec.audio.layout cimport AudioLayout
from quickcodec.filter.graph cimport Graph


cdef class AudioResampler:

    cdef readonly bint is_passthrough

    cdef AudioFrame template

    # Destination descriptors
    cdef readonly AudioFormat format
    cdef readonly AudioLayout layout
    cdef readonly int rate
    cdef readonly unsigned int frame_size

    cdef Graph graph

    cpdef resample(self, AudioFrame)
