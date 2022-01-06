from logging import getLogger, DEBUG, StreamHandler, Formatter

from logging_example.t.a import awork
from logging_example.t.b import bwork

if __name__ == "__main__":

    log = getLogger("logging_example.t")
    log.setLevel(DEBUG)
    console = StreamHandler()
    console.setFormatter(Formatter("%(asctime)s [%(levelname)s] - %(message)s"))
    log.addHandler(console)

    awork()
    bwork()
