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
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    length = len(str(num))
    if length > 1:
        first = int(str(num)[0])
        second = int(str(num)[1])

    if 0 < num < 10:
        robot_speech = FIRST_TEN[num - 1]

    elif length == 2:
        robot_speech = find_speech_for_double_num(num, first, second)

    else:
        third = int(str(num)[2])
        robot_speech =  FIRST_TEN[first - 1] + " " + HUNDRED
        if num % 100 == 0:
            return robot_speech
        elif str(second) + str(third) == '10':
            robot_speech += " " + SECOND_TEN[0]
        elif num % 10 == 0:
            robot_speech += " " + OTHER_TENS[second - 2]
        elif second == 0:
            robot_speech += " " + FIRST_TEN[third - 1]
        elif second == 1:
            robot_speech += " " + SECOND_TEN[int(str(num)[1:]) % 10]
        else:
            robot_speech += " " + OTHER_TENS[second - 2] + " " + FIRST_TEN[third - 1]

    return robot_speech


def find_speech_for_double_num(num: int, first: int, second: int) -> str:

    is_num_before_twenty = 10 <= num < 20
    is_zero_div_by_10 = num % 10 == 0
    num_after_twenty_condition = OTHER_TENS[num // 10 - 2] if is_zero_div_by_10 else \
        OTHER_TENS[first - 2] + " " + FIRST_TEN[second - 1]

    return SECOND_TEN[num % 10] if is_num_before_twenty else num_after_twenty_condition
