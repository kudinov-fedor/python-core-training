"""
****** Task3 ********************************************************
Sum Numbers

In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
*********************************************************************
"""


def sum_numbers(text: str) -> int:
    result_list = []

    # edge cases
    words_list = text.split(" ")
    if len(words_list) == 1 and not words_list[0].isdigit():
        return sum(result_list)

    # final steps
    for i in words_list:
        if i.isdigit():
            result_list.append(int(i))

    return sum(result_list)


assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year")
    == 3755)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0
