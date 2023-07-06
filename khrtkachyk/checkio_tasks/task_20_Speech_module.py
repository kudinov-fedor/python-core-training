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

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
              "eighteen", "nineteen", ]
OTHER_TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
HUNDRED = "hundred"


def checkio_1_0(num: int) -> str:
    word = ""
    if num == 0:
        return "zero"
    if num == 1000:
        word += FIRST_TEN[(num // 1000) - 1] + " thousand "
    num %= 1000
    if num >= 100:
        word += FIRST_TEN[(num // 100) - 1] + " hundred "
    num = num % 100
    if 10 <= num <= 19:
        word += SECOND_TEN[num - 10] + " "
    elif num:
        if num >= 20:
            word += OTHER_TENS[num - num % 10] + " "
        num = num % 10
        if num >= 1:
            word += FIRST_TEN[num - 1] + " "
    return word.strip()
