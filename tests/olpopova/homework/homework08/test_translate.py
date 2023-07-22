import pytest

from olpopova.homework.homework08.bird_translation_phrase import translate, translate_with_table


@pytest.mark.parametrize(['text', 'expected'], [
    ("hieeelalaooo", "hello"),
    ("hoooowe yyyooouuu duoooiiine", "how you doin"),
    ("aaa bo cy da eee fe", "a b c d e f"),
    ("sooooso aaaaaaaaa", "sos aaa"),
    ('tyooo bieee ooora nyooote tiooo byeee', 'to be or not to be'),
    ('baliaaa bolaaaa boloaaa baloaaa', 'bla bla bla bla'),
    ('doooo yyyooouuu sapieeeaaaky eeenugaleiiisyhy', 'do you speak english')
])
def test_translate(text, expected):
    assert translate(text) == translate_with_table(text) == expected
