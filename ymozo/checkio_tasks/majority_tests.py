import pytest
import majority


@pytest.mark.parametrize(["param", "result"], [
    ([True, True, False, True, False], True),
    ([True, True, False], True),
    ([True, True, False, False], False),
    ([True, True, False, False, False], False),
    ([False], False),
    ([True], True),
    ([], False)
])
def test_majority(param, result):
    is_majority = majority.is_majority(param)
    assert is_majority == result
