import pytest


def three_in_row(text):
    count = 0
    for elem in text.split():
        if not elem.isdigit():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


@pytest.mark.parametrize("text, expected_result", [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True)
])
def test_three_in_row(text, expected_result):
    assert three_in_row(text) == expected_result
