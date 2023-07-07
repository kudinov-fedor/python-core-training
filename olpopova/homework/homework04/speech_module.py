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
    # edge case
    if num == 0:
        return "zero"

    length = len(str(num))

    #  find hundred
    hundred = FIRST_TEN[num // 100 - 1] + " " + HUNDRED if length == 3 else ''

    # find dozen word for '3-' or '2-' digit number
    dozen_number = num % 100 if length == 3 else num
    temp_dozen = SECOND_TEN[num % 10] if dozen_number // 10 == 1 else OTHER_TENS[dozen_number // 10 - 2]
    dozen = temp_dozen if len(str(dozen_number).lstrip('0')) == 2 else ''

    # find unit
    unit_number = num if length == 1 else dozen_number % 10
    unit = FIRST_TEN[unit_number - 1] if not unit_number == 0 and not 10 < dozen_number < 20 else ''

    return (hundred + " " + dozen + " " + unit).strip().replace("  ", " ")
