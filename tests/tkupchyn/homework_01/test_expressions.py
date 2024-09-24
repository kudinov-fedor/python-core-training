import pytest

@pytest.mark.parametrize('string, expected_result', [('abc', 'a|b|c'),
                                                     ('test', 't|e|s|t'),])
def test_string_join(string, expected_result):
    result = str.join("|", string)
    assert result == expected_result


@pytest.mark.parametrize('words, expected_result', [(['abc', '', 'banana', 'ball'], 'banana'),
                                                   (['test', '123123124'], '123123124'),
                                                    ([], ValueError),
                                                    (['test', 'with', True], ValueError)])
def test_longest_word(words, expected_result):
    if not words or not all(isinstance(word, str) for word in words):
        with pytest.raises(ValueError):
            raise ValueError("No words provided")
    else:
        result = max(words, key=len)
        assert result == expected_result



