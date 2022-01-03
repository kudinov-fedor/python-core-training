from logging import getLogger, StreamHandler

console = getLogger(__name__)
console.addHandler(StreamHandler())


def do(show_error):
    try:
        raise RuntimeError("some error")
    except RuntimeError:
        console.error("The error!")
        if show_error:
            console.exception("Will handle the error below!")
        console.warning("Done!")


do(False)
