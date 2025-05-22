import errno
import logging
import threading

import quickcodec.error
import quickcodec.logging


def do_log(message: str) -> None:
    quickcodec.logging.log(quickcodec.logging.INFO, "test", message)


def test_adapt_level() -> None:
    assert quickcodec.logging.adapt_level(quickcodec.logging.ERROR) == logging.ERROR
    assert quickcodec.logging.adapt_level(quickcodec.logging.WARNING) == logging.WARNING
    assert (
        quickcodec.logging.adapt_level((quickcodec.logging.WARNING + quickcodec.logging.ERROR) // 2)
        == logging.WARNING
    )


def test_threaded_captures() -> None:
    quickcodec.logging.set_level(quickcodec.logging.VERBOSE)

    with quickcodec.logging.Capture(local=True) as logs:
        do_log("main")
        thread = threading.Thread(target=do_log, args=("thread",))
        thread.start()
        thread.join()

    assert (quickcodec.logging.INFO, "test", "main") in logs
    quickcodec.logging.set_level(None)


def test_global_captures() -> None:
    quickcodec.logging.set_level(quickcodec.logging.VERBOSE)

    with quickcodec.logging.Capture(local=False) as logs:
        do_log("main")
        thread = threading.Thread(target=do_log, args=("thread",))
        thread.start()
        thread.join()

    assert (quickcodec.logging.INFO, "test", "main") in logs
    assert (quickcodec.logging.INFO, "test", "thread") in logs
    quickcodec.logging.set_level(None)


def test_repeats() -> None:
    quickcodec.logging.set_level(quickcodec.logging.VERBOSE)

    with quickcodec.logging.Capture() as logs:
        do_log("foo")
        do_log("foo")
        do_log("bar")
        do_log("bar")
        do_log("bar")
        do_log("baz")

    logs = [log for log in logs if log[1] == "test"]

    assert logs == [
        (quickcodec.logging.INFO, "test", "foo"),
        (quickcodec.logging.INFO, "test", "foo"),
        (quickcodec.logging.INFO, "test", "bar"),
        (quickcodec.logging.INFO, "test", "bar (repeated 2 more times)"),
        (quickcodec.logging.INFO, "test", "baz"),
    ]

    quickcodec.logging.set_level(None)


def test_error() -> None:
    quickcodec.logging.set_level(quickcodec.logging.VERBOSE)

    log = (quickcodec.logging.ERROR, "test", "This is a test.")
    quickcodec.logging.log(*log)
    try:
        quickcodec.error.err_check(-errno.EPERM)
    except quickcodec.error.PermissionError as e:
        assert e.log == log
    else:
        assert False

    quickcodec.logging.set_level(None)
