import pytest


@pytest.mark.parametrize(['numbers', 'expected'], [
    ([2, 3, 1, -2, -12], -12),
    ([23, -5, 4], 23),
])
def test_max_modulo_number(numbers, expected):
    max_module_value = max(numbers, key=abs)
    assert max_module_value is expected


@pytest.mark.parametrize(['words', 'expected'], [
    (["crocodile", "ball", "cat", 'zorro'], 9),
    (['elephant', 'sea', 'beach'], 8)
])
def test_max_chars_in_word(words, expected):
    max_module_value = len(max(words, key=len))
    assert max_module_value is expected


@pytest.mark.parametrize(['actual_list', 'expected'], [
    (["banana", "ball", "cat", 'zorro'], "zorro"),
    ([True, False], True),
    ([1, 7, 55], 55),
    ([], '')
])
def test_max_value_in_list(actual_list, expected):
    if len(actual_list) != 0:
        max_word = max(actual_list)
        assert max_word is expected
    else:
        print("\n**** List is empty! ****")


@pytest.mark.parametrize(['actual', 'reverse', 'expected'], [
    ([2, 4, -5, 6, -1], "True", [6, 4, 2, -1, -5]),
    ([2, 4, -5, 6, -1], "False", [-5, -1, 2, 4, 6]),
    ([2, 4, -5, 6, -1], "module", [-1, 2, 4, -5, 6])
])
def test_sort_numbers(actual, reverse, expected):
    if reverse == "True":
        changed_list = sorted(actual, reverse=True)
    elif reverse == "False":
        changed_list = sorted(actual)
    else:
        changed_list = sorted(actual, key=abs)
    assert changed_list == expected


def test_find_ascii_integer(values_list):
    # sth = []
    for string in values_list:
        # map = (*map(ord, string), sep='_')
        print(*map(ord, string), sep=', ')
        # print('Chars in {} has following numbers in ASCII table [{}]'.format(string)
    # print(srt)


@pytest.mark.parametrize(['actual', 'sort_type','expected'], [
    (["banana", "ball", "cat"], 'alphabet', ["ball", "banana", "cat"]),
    (["banana", "ball", "cat"], 'words_length', ["cat", "ball", "banana"]),
    (["banana", "ball", "cat"], 'reverse', ["cat", "banana", "ball"]),
    (["banana", "ball", "cat"], "reverse_and_length", ["banana", "ball", "cat"])
])
def test_sort_chars(actual, sort_type, expected):
    if sort_type == 'alphabet':
        changed_list = sorted(actual)
    elif sort_type == 'words_length':
        changed_list = sorted(actual, key=len)
    elif sort_type == 'reverse':
        changed_list = sorted(actual, reverse=True)
    else:
        changed_list = sorted(actual, reverse=True, key=len)
    assert changed_list == expected
