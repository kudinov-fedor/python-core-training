"""
You are given a string with words and numbers separated by whitespaces (one space).
The words contain only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string (str) with words.
Output: Logic value (bool).
"""


def checkio(words: str) -> bool:
    n = 3
    lst = words.split()
    start = 0
    for word in lst:
        if word.isalpha():
            start += 1
        else:
            start = 0
        if start >= n:
            return True
    return False


def checkio1_2(words: str) -> bool:
    lst = words.split()
    return any(all(map(str.isalpha, lst[index:index + 3])) for index in range(len(lst) - 2))


def checkio_2(words: str) -> bool:
    words = words.split()
    window_size = 3
    if len(words) < window_size:
        return False
    for i in range(len(words) - window_size + 1):
        res = words[i:i + window_size]
        if all(map(str.isalpha, res)):
            return True
    return False


def checkio_3(words: str) -> bool:
    split = words.split()
    return any(all(map(str.isalpha, three_words)) for three_words in (zip(split, split[1:], split[2:])))
