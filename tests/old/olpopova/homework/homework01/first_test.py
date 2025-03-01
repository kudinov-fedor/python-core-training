import pytest


@pytest.mark.parametrize(['numbers', 'expected'], [
    ([2, 3, 1, -2, -12], -12),
    ([23, -5, 4], 23),
])
def test_max_modulo_number(numbers, expected):
    max_module_value = max(numbers, key=abs)
    assert max_module_value == expected


@pytest.mark.parametrize(['words', 'expected'], [
    (["crocodile", "ball", "cat", 'zorro'], 9),
    (['elephant', 'sea', 'beach'], 8)
])
def test_max_chars_in_word(words, expected):
    max_module_value = len(max(words, key=len))
    assert max_module_value == expected


@pytest.mark.parametrize(['actual_list', 'expected'], [
    (["banana", "ball", "cat", 'zorro'], "zorro"),
    ([True, False], True),
    ([1, 7, 55], 55),
    ([], '')
])
def test_max_value_in_list(actual_list, expected):
    if len(actual_list) != 0:
        max_word = max(actual_list)
        assert max_word == expected


@pytest.mark.parametrize(['actual', 'reverse', 'expected'], [
    ([2, 4, -5, 6, -1], True, [6, 4, 2, -1, -5]),
    ([2, 4, -5, 6, -1], False, [-5, -1, 2, 4, 6]),
    ([2, 4, -5, 6, -1], None, [-5, -1, 2, 4, 6])
])
def test_sort_numbers_reverse_param(actual, reverse, expected):
    kwargs = {}
    if reverse is not None:
        kwargs['reverse'] = reverse
    changed_list = sorted(actual, **kwargs)
    assert changed_list == expected


@pytest.mark.parametrize(['value', 'expected'], [
    ("banana", [98, 97, 110, 97, 110, 97]),
    ("cat", [99, 97, 116])
])
def test_find_ascii_integer(value, expected):
    assert list(map(ord, value)) == expected


@pytest.mark.parametrize(['actual', 'reverse', 'length', 'expected'], [
    (["banana", "ball", "cat"], False, False, ["ball", "banana", "cat"]),
    (["banana", "ball", "cat"], False, True, ["cat", "ball", "banana"]),
    (["banana", "ball", "cat"], True, False, ["cat", "banana", "ball"]),
    (["banana", "ball", "cat"], True, True, ["banana", "ball", "cat"])
])
def test_sort_chars_reverse_len_params(actual, reverse, length, expected):
    kwargs = {'reverse': reverse}
    if length:
        kwargs['key'] = len
    changed_list = sorted(actual, **kwargs)
    assert changed_list == expected
