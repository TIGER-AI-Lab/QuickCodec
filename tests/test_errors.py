import errno
from traceback import format_exception_only

import quickcodec

from .common import is_windows


def test_stringify() -> None:
    for cls in (quickcodec.ValueError, quickcodec.FileNotFoundError, quickcodec.DecoderNotFoundError):
        e = cls(1, "foo")
        assert f"{e}" == "[Errno 1] foo"
        assert f"{e!r}" == f"{cls.__name__}(1, 'foo')"
        assert (
            format_exception_only(cls, e)[-1]
            == f"av.error.{cls.__name__}: [Errno 1] foo\n"
        )

    for cls in (quickcodec.ValueError, quickcodec.FileNotFoundError, quickcodec.DecoderNotFoundError):
        e = cls(1, "foo", "bar.txt")
        assert f"{e}" == "[Errno 1] foo: 'bar.txt'"
        assert f"{e!r}" == f"{cls.__name__}(1, 'foo', 'bar.txt')"
        assert (
            format_exception_only(cls, e)[-1]
            == f"av.error.{cls.__name__}: [Errno 1] foo: 'bar.txt'\n"
        )


def test_bases() -> None:
    assert issubclass(quickcodec.ValueError, ValueError)
    assert issubclass(quickcodec.ValueError, quickcodec.FFmpegError)

    assert issubclass(quickcodec.FileNotFoundError, FileNotFoundError)
    assert issubclass(quickcodec.FileNotFoundError, OSError)
    assert issubclass(quickcodec.FileNotFoundError, quickcodec.FFmpegError)


def test_filenotfound():
    """Catch using builtin class on Python 3.3"""
    try:
        quickcodec.open("does not exist")
    except FileNotFoundError as e:
        assert e.errno == errno.ENOENT
        if is_windows:
            assert e.strerror in (
                "Error number -2 occurred",
                "No such file or directory",
            )
        else:
            assert e.strerror == "No such file or directory"
        assert e.filename == "does not exist"
    else:
        assert False, "No exception raised!"


def test_buffertoosmall() -> None:
    """Throw an exception from an enum."""

    BUFFER_TOO_SMALL = 1397118274
    try:
        quickcodec.error.err_check(-BUFFER_TOO_SMALL)
    except quickcodec.error.BufferTooSmallError as e:
        assert e.errno == BUFFER_TOO_SMALL
    else:
        assert False, "No exception raised!"
