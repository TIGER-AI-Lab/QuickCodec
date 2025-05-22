from quickcodec.buffer cimport Buffer
from quickcodec.frame cimport Frame


cdef class Plane(Buffer):

    cdef Frame frame
    cdef int index

    cdef size_t _buffer_size(self)
    cdef void* _buffer_ptr(self)
