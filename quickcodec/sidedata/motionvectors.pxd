cimport libav as lib

from quickcodec.frame cimport Frame
from quickcodec.sidedata.sidedata cimport SideData


cdef class _MotionVectors(SideData):

    cdef dict _vectors
    cdef int _len


cdef class MotionVector:

    cdef _MotionVectors parent
    cdef lib.AVMotionVector *ptr
