import pytest

from ihontaryk.homework_4.string_methods import find_special_characters


@pytest.mark.parametrize('text, expected_result',
                         [('ro&%$ 99 _+# ta%tor', 'In this text were found such special characters: # $ % & + _'),
                          ('leve^&^ !@!hhl', 'In this text were found such special characters: ! & @ ^'),
                          ('ban   ana', 'In this text were not found special characters'),
                          ('ra()()( cecar', 'In this text were found such special characters: ( )')])
def test_find_special_characters(text, expected_result):
    """
    verify find_special_characters function
    """

    assert find_special_characters(text) == expected_result
