import pytest


@pytest.mark.parametrize('data, expected_result', [
    ('abc', 3),
    (['a', 'b', 'CDEFG'], 3),
    ({1: 'Some', 2: 'test', 3: 'data'}, 3)
])
def test_len(data, expected_result):
    """Verify length of various data types"""
    assert len(data) == expected_result
