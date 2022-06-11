import pytest, os


PLATFORM = os.environ.get("PLATFORM", 'web')


CAPS = [
    ("chrome", "L"),
    ("chrome", "M"),
    ("chrome", "S"),
    ("firefox", "L"),
    ("firefox", "M"),
    ("firefox", "S"),
    ("safari", "L"),
    ("safari", "M"),
    ("safari", "S"),
]

if PLATFORM == "mobile":
    CAPS = [
        ("mobile", "L")
    ]


@pytest.fixture(params=CAPS, ids=[str(i) for i in CAPS])
def driver(request):
    return request.param


# def pytest_addoption(parser):
#     parser.addoption("--all", action="store_true", help="run all combinations")
#
#
# def pytest_generate_tests(metafunc):
#     if "driver" in metafunc.fixturenames:
#         if metafunc.config.getoption("all"):
#             caps = CAPS
#         else:
#             caps = CAPS[:1]
#         metafunc.parametrize("driver", caps, ids=[str(i) for i in caps])
