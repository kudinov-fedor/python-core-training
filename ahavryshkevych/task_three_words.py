"""
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contain only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.
"""


def three_words(words: str) -> bool:
    match = 0
    for el in words.split():
        if el.isalpha():
            match += 1
        else:
            match = 0
        if match >= 3:
            return True
    return False


def three_words02(words: str) -> bool:
    spl_words = [i for i in words.split()]
    for word1, word2, word3 in zip(spl_words, spl_words[1:], spl_words[2:]):
        if word1.isalpha() and word2.isalpha() and word3.isalpha():
            return True
    return False
