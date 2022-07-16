
from collections import Counter
from typing import Iterable

def first_word(text: str) -> str:
    return text.split()[0]


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


def number_length(a: int) -> int:
    return len(str(a))


def most_frequent(data: list) -> str:
    data_collection = Counter(data)
    return max(data_collection.items(), key=lambda x: x[1])[0]


def backward_string(val: str) -> str:
    return val[::-1]


def end_zeros(num: int) -> int:
    data = str(num)
    return  0 if data[-1] != '0' else len(data) - len(data.rstrip('0'))


def easy_unpack(elements: tuple) -> tuple:
    return (elements[0], elements[2], elements[-2])


def remove_all_before(items: list, border: int) -> Iterable:
    return items if border not in items else items[items.index(border):]

# def is_all_upper(text: str) -> bool:
#     return text.isupper() |

def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1]


def max_digit(number: int) -> int:
    string_number = str(number)
    return max([int(i) for i in string_number])


def beginning_zeros(number: str) -> int:
    return len(str(number)) - len(str(number).lstrip('0'))


def between_markers(text: str, begin: str, end: str):
    first_index = text.find(begin) + 1
    second_index = text.find(end)
    return text[first_index:second_index]

# def split_pairs(a: str):


def correct_sentence(text: str) -> str:
    return text.capitalize() if text[-1] == '.' else text.capitalize() + '.'

def is_even(num: int) -> bool:
    return num%2 ==0

# def nearest_value(values: set, one: int) -> int:
