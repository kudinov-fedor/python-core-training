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
THOUSAND = "thousand"


def first_ten(number, denom, word):
    return FIRST_TEN[(number // denom) - 1] + " " + word + " "


def checkio_1_0(num: int) -> str:
    word = ""
    if num == 0:
        return "zero"
    if num == 1000:
        word += first_ten(num, 1000, THOUSAND)
    hundreds = num % 1000
    if hundreds >= 100:
        word += first_ten(hundreds, 100, HUNDRED)
    teens_and_tens = num % 100
    if 10 <= teens_and_tens <= 19:
        word += SECOND_TEN[teens_and_tens - 10] + " "
    elif teens_and_tens:
        if teens_and_tens >= 20:
            word += OTHER_TENS[teens_and_tens - teens_and_tens % 10] + " "
        ones = teens_and_tens % 10
        if ones >= 1:
            word += FIRST_TEN[ones - 1] + " "
    return word.strip()


FIRST_TEN2 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
               "nineteen"]
OTHER_TENS2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED2 = "hundred"
THOUSAND2 = "thousand"


def checkio_2_0(num: int) -> str:
    hundreds, before_hundred = divmod(num, 100)
    tens, ones = divmod(before_hundred, 10)

    resulting = []
    if num == 0:
        resulting.append("zero")
        return ' '.join(resulting)
    if num == 1000:
        resulting.append(THOUSAND2)
        return ' '.join(resulting)

    if hundreds:
        resulting.extend([FIRST_TEN2[hundreds], HUNDRED2])
        num = before_hundred

    if before_hundred >= 20:
        resulting.append(OTHER_TENS2[tens - 2])
        num = ones

    if num >= 10:
        teens = num - 10
        resulting.append(SECOND_TEN2[teens])

    elif ones > 0:
        resulting.append(FIRST_TEN2[ones])
    return ' '.join(resulting)
