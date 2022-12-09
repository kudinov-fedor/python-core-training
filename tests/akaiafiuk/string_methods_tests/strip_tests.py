def test_strip_no_args():
    """Strip with no args returns a copy of the string with leading and trailing whitespace removed."""
    some_string = "    Hello There    "
    assert some_string.strip() == "Hello There"


def test_strip_with_args():
    """If chars is given and not None, remove characters in chars instead."""
    some_string = "xyyxyxx    Hello xy There    yxyxyxyxyyxxyyyx"
    assert some_string.strip("xy") == "    Hello xy There    "
