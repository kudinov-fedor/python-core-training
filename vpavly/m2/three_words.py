"""
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession . For example, the string "start 5 one two three 7 end"
contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.
"""


def three_words_in_succession(text: str) -> bool:
    result = 0
    for i in text.split():
        if result >= 3:
            break
        else:
            if i.isalpha():
                result += 1
            else:
                result = 0
    return result >= 3
