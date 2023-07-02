"""
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contain only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.
"""


def three_words(words: str) -> bool:
    match = 0
    for el in words.split(" "):
        if el.isalpha():
            match += 1
        else:
            match = 0
        if match >= 3:
            return True
    return False
