"""
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession . For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Example:

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
1
2
3
4
How it is used: This teaches you how to work with strings and introduces some useful functions.
"""


def is_three_words(words: str) -> bool:
    counter = 0
    for word in words.split():
        if word.isalpha():
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return True
    return False


def is_three_words_bool(words: str) -> bool:
    count = 0
    for word in words.split():
        count = (count + 1) * word.isalpha()
        if count == 3:
            return True
    return False
