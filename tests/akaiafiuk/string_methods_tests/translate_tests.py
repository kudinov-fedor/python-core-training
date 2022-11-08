import pytest


@pytest.fixture
def some_string():
    return "Say hello to anton."


def test_using_dict(some_string):
    """Use a dictionary with decimal ascii codes to replace 65 (A) with 64 (@)"""
    translate_dict = {97: 64}
    assert some_string.translate(translate_dict) == "S@y hello to @nton."


def test_using_dict_replace_to_none(some_string):
    """Can remove characters by replacing them to None in the dict"""
    translate_dict = {
        108: None,        # Replace l with None
        111: None,        # Replace o with None
        97: 64,           # replace 65 (A) with 64 (P)
    }
    assert some_string.translate(translate_dict) == "S@y he t @ntn."


def test_using_mapping_table(some_string):
    """Create mapping table using maketrans and then translate using this table"""
    original = "Say"
    translated = "$@Y"
    table = some_string.maketrans(original, translated)
    translated = some_string.translate(table)
    assert table == {83: 36, 97: 64, 121: 89}   # Basically, maketrans() creates a translate dict
    assert translated == "$@Y hello to @nton."  # And then characters are replaced using this dict


def test_errors_different_len(some_string):
    """Error is thrown in case when maketrans arguments have different length"""
    original = "Say"
    translated = "$@Y1"
    with pytest.raises(ValueError, match="the first two maketrans arguments must have equal length"):
        some_string.maketrans(original, translated)


def test_errors_different_type(some_string):
    """Error is thrown in case when maketrans arguments are not str"""
    original = "Say"
    translated = 123
    with pytest.raises(TypeError, match="must be str, not int"):
        some_string.maketrans(original, translated)
