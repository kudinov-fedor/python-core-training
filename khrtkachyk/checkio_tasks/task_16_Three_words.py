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


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World hello"))
    print(checkio("bla bla bla bla"))
    print(checkio("He is 123 man"))
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
