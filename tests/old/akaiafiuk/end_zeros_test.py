import pytest
from akaiafiuk.end_zeros import (end_zeros, end_zeros_using_split, end_zeros_using_zip, end_zeros_using_generator,
                                 end_zeros_using_translate)


@pytest.mark.parametrize("func", [
    end_zeros,
    end_zeros_using_split,
    end_zeros_using_zip,
    end_zeros_using_generator,
    end_zeros_using_translate
])
@pytest.mark.parametrize("in_param, expected_result", [
    (0, 1),
    (1, 0),
    (10, 1),
    (101, 0),
    (245, 0),
    (100100, 2),
    (1234567890000, 4)
])
def test_all_end_zeros_functions(func, in_param, expected_result):
    assert func(in_param) == expected_result
