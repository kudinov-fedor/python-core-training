from aoleshko.is_acceptable_password import is_acceptable_password


def test_is_acceptable_password():
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('much-longer') is True
