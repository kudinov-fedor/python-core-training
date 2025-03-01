import string
import statistics
from statistics import mode

# You should return a given string in reverse order


def backward_string(text: str) -> str:
    my_str = list(reversed(text))
    my_lst_str = ''.join(map(str, my_str))
    return my_lst_str


# return the number of times the value appears in the string


def count_value(a, sub):
    return a.count(sub)


# create a function that gets a tuple and returns a tuple with 3 elements - the first,
# third and second element from the last for the given array.


def easy_unpack(element: tuple) -> tuple:
    e1 = element[0]
    e3 = element[2]
    el1 = element[-2]
    return e1, e3, el1


# Try to find out how many zeros a given number has at the end.


def end_zeros(num: int) -> int:
    text = str(num)
    return len(text) - len(text.strip('0'))


# verification adding new items at the end of the list


def extend_func(a: list, b: list) -> list:
    result = a.extend(b)
    return a


# find first word (without spaces in the start)


def first_word(text: str) -> str:
    result = text.split(" ")
    return result[0]


# password the length should be bigger than 6


def is_acceptable_pass(text: str) -> bool:
    return len(text) > 6


# verification that all the characters in the text are digits


def isdigit_func(txt: str) -> str:
    return txt.isdigit()


# number length


def number_length(a: int) -> int:
    num = str(a)
    return len(num)


# find the most frequent string in the list


def most_frequent(a: list):
    return mode(a)
