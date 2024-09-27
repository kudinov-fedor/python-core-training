import pytest


@pytest.mark.parametrize('string, expected_result', [('abc', 'a|b|c'),
                                                     ('test', 't|e|s|t')])
def test_string_join(string, expected_result):
    result = str.join("|", string)
    assert result == expected_result


@pytest.mark.parametrize('words, expected_result', [(['abc', '', 'banana', 'ball'], 'banana'),
                                                    (['test', '123123124'], '123123124')])
def test_longest_word_positive(words, expected_result):
    result = max(words, key=len)
    assert result == expected_result


@pytest.mark.parametrize('words', [([1, 3, "error", True])])
def test_longest_word_negative(words):
    with pytest.raises(TypeError,):
        max(words, key=len)
