"""
Case, when global var is dynamically created

"""


def modify_global(key, value):
    globals()[key] = value


def get_global(key):
    return globals()[key]


if __name__ == "__main__":

    modify_global("some", 123)
    assert get_global("some") == 123
    assert some == 123
