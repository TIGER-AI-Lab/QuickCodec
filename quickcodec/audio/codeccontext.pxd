
from quickcodec.audio.frame cimport AudioFrame
from quickcodec.audio.resampler cimport AudioResampler
from quickcodec.codec.context cimport CodecContext


cdef class AudioCodecContext(CodecContext):
    # Hold onto the frames that we will decode until we have a full one.
    cdef AudioFrame next_frame
    # For encoding.
    cdef AudioResampler resampler
