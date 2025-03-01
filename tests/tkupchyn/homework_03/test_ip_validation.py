import pytest
from tkupchyn.homework_03.ip_validation import is_valid_ip


@pytest.mark.parametrize("ip_address, expected_result",
                         [
                             ('12.255.56.1', True),
                             ('', False),
                             ('abc.def.ghi.jkl', False),
                             ('123.456.789.0', False),
                             ('12.34.56', False),
                             ('12.34.56 .1', False),
                             ('12.34.56.-1', False),
                             ('123.045.067.089', False),
                             ('127.1.1.0', True),
                             ('0.0.0.0', True),
                             ('0.34.82.53', True),
                             ('192.168.1.300', False),
                         ])
def test_is_valid_ip(ip_address, expected_result):
    assert is_valid_ip(ip_address) == expected_result
