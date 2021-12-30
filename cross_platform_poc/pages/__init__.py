import os

PLATFORM = os.environ.get("PLATFORM", "web")


# __path__.append(os.path.join(os.path.dirname(__file__), PLATFORM))
#
# from .pages import *


if PLATFORM == "web":
    from .web.pages import *
elif PLATFORM == "mobile":
    from .mobile.pages import *
