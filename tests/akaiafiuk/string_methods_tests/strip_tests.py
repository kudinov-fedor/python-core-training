def test_strip_no_args():
    """Strip with no args returns a copy of the string with leading and trailing whitespace removed."""
    some_string = "    Hello There    "
    assert some_string.strip() == "Hello There"  # A new string is returned
    assert some_string == "    Hello There    "  # Original string is not changed


def test_strip_with_args():
    """If chars is given and not None, remove characters in chars instead."""
    some_string = "xxx    Hello xy There    yyy"
    assert some_string.strip("xy") == "    Hello xy There    "
