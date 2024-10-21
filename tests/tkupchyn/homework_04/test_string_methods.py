import pytest


def test_format_string():
    pattern = "{second} {first}"
    attrs = {"first": "world", "second": "hello", "other": "some"}
    assert pattern.format(**attrs) == "hello world"


@pytest.mark.parametrize("word, suffix, expected_result",
                         (
                                 ('useless', 'less', 'use'),
                                 ('quickly', 'ly', 'quick'),
                                 ('movement', 'ment', 'move')
                         ))
def test_removesuffix(word, suffix, expected_result):
    assert word.removesuffix(suffix) == expected_result
