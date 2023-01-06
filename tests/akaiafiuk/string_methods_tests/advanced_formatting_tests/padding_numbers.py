def test_int_specific_width():
    """An int can be constraint to the specific width"""
    assert f"{42:4d}" == "  42"


def test_float_specific_width():
    """An int can be constraint to the specific width"""
    assert f"{42.024:10.1f}" == "      42.0"


def test_fixed_number_of_characters():
    """In the example below we want our output to have at least 6 characters with 2 after the decimal point."""
    assert f"{42.024:010.1f}" == "00000042.0"
