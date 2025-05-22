cimport libav as lib

from quickcodec.container.core cimport Container
from quickcodec.stream cimport Stream


cdef class InputContainer(Container):

    cdef flush_buffers(self)
