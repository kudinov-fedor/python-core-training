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
    my_tuple = tuple(i for i in words.split())
    for word1, word2, word3 in zip(my_tuple, my_tuple[1:], my_tuple[2:]):
        res = word1 + word2 + word3
        if all(map(str.isalpha, res)):
            return any(j for j in map(str.isalpha, res) if j is True)
    return False


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World hello"))
    print(checkio("bla bla bla bla"))
    print(checkio("He is 123 man"))
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

    print("Example:")
    print(checkio_2("Hello World hello"))
    print(checkio_2("bla bla bla bla"))
    print(checkio_2("He is 123 man"))
    print(checkio_2("one two 3 four five six 7 eight 9 ten eleven 12"))
    print(checkio_2('one two 3 four five 6 seven eight 9 ten eleven 12'))

    print("Example:")
    print(checkio_3("Hello World hello"))
    print(checkio_3("bla bla bla bla"))
    print(checkio_3("He is 123 man"))
    print(checkio_3("one two 3 four five six 7 eight 9 ten eleven 12"))
    print(checkio_3('one two 3 four five 6 seven eight 9 ten eleven 12'))
