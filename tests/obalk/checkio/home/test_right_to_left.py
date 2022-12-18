import pytest

from obalk.checkio.home.right_to_left import right_to_left


@pytest.mark.parametrize("phrases, result", [
    (("left", "right", "left", "stop"), "left,left,left,stop"),
    (("bright aright", "ok"), "bleft aleft,ok")
])
def test_right_to_left(phrases, result):
    assert right_to_left(phrases) == result
