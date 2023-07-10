"""
**********************************************************************
Speech Module

Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input
all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to
speak properly and increase his number processing speed by writing a new speech module for him. All the words in the
string must be separated by exactly one space character. Be careful with spaces - it's hard to see if you place two
spaces instead one.
**********************************************************************
"""

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
              "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    res = []

    # edge case
    if num == 0:
        return "zero"

    hundred, other = divmod(num, 100)
    if hundred:
        hundred_word = FIRST_TEN[hundred - 1] + " " + HUNDRED
        res.append(hundred_word)

    dozen, unit = divmod(other, 10)
    if dozen:
        dozen_word = SECOND_TEN[unit] if other in range(10, 20) else OTHER_TENS[dozen - 2]
        res.append(dozen_word)

    if unit and not other in range(10, 20):
        unit_word = FIRST_TEN[unit - 1]
        res.append(unit_word)

    return " ".join(res)
