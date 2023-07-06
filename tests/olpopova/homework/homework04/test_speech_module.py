import pytest

from olpopova.homework.homework04.speech_module import checkio


@pytest.mark.parametrize(['number', 'expected'], [
    (1, "one"),
    (2, "two"),
    (310, "three hundred ten"),
    (3, "three"),
    (4, "four"),
    (5, "five"),
    (6, "six"),(9, "nine"),
    (10, "ten"),
    (11, "eleven"),
    (12, "twelve"),
    (13, "thirteen"),
    (14, "fourteen"),
    (15, "fifteen"),
    (16, "sixteen"),
    (17, "seventeen"),
    (18, "eighteen"),
    (19, "nineteen"),
    (999, "nine hundred ninety nine"),
    (784, "seven hundred eighty four"),
    (777, "seven hundred seventy seven"),
    (88, "eighty eight"),
    (44, "forty four"),
    (20, "twenty"),
    (30, "thirty"),
    (40, "forty"),
    (50, "fifty"),
    (80, "eighty"),
    (90, "ninety"),
    (100, "one hundred"),
    (200, "two hundred"),
    (300, "three hundred"),
    (600, "six hundred"),
    (700, "seven hundred"),
    (900, "nine hundred"),
    (21, "twenty one"),
    (312, "three hundred twelve"),
    (302, "three hundred two"),
    (509, "five hundred nine"),
    (753, "seven hundred fifty three"),
    (940, "nine hundred forty")
])
def test_speech_module(number, expected):
    assert checkio(number) == expected
