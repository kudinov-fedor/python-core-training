import pytest
from obalk.checkio.initiation.the_most_frequent_letter import most_frequent, most_frequent_with_max


@pytest.mark.parametrize("function", [most_frequent, most_frequent_with_max])
@pytest.mark.parametrize("data, result", [
    (["a", "b", "c", "a", "b", "a"], "a"),
    (["a", "a", "bi", "bi", "bi"], "bi")])
def test_most_frequent(function, data, result):
    assert function(data) == result
