import pytest
from checkio_tasks.task_20_Speech_module import checkio_1_0, checkio_2_0
"""
Stephen's speech module is broken. This module is responsible for his number pronunciation.
He has to click to input all the numerical digits in a figure, so when there are big
numbers it can take him a long time. Help the robot to speak properly and increase his number
processing speed by writing a new speech module for him. All the words in the string must be separated
by exactly one space character. Be careful with spaces - it's hard to see if you place two spaces instead one.

Input: An integer (int).
Output: A string (str).
Precondition:0 < number < 1000

"""


@pytest.mark.parametrize("func", [checkio_1_0, checkio_2_0])
@pytest.mark.parametrize("num, res", [
    (1, "one"),
    (2, "two"),
    (3, "three"),
    (4, "four"),
    (5, "five"),
    (6, "six"),
    (9, "nine"),
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
    (315, "three hundred fifteen"),
    (302, "three hundred two"),
    (509, "five hundred nine"),
    (753, "seven hundred fifty three"),
    (940, "nine hundred forty"),
    (999, "nine hundred ninety nine")
])
def test_speech_module(func, num, res):
    assert func(num) == res
