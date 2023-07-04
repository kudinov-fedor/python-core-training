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
    res = bool([index for index in range(len(lst) - 2) if all(map(str.isalpha, lst[index:index + 3]))])
    return res


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
    res = bool([(word1, word2, word3) for (word1, word2, word3) in (zip(split, split[1:], split[2:])) if
                str(word1 + word2 + word3).isalpha()])
    return res


if __name__ == '__main__':
    # print("Example:")
    # print(checkio("Hello World hello"))
    # print(checkio("bla bla bla bla"))
    # print(checkio("He is 123 man"))
    # print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
    #
    # print("Example:")
    # print(checkio1_2("Hello World hello"))
    # print(checkio1_2("bla bla bla bla"))
    # print(checkio1_2("He is 123 man"))
    # print(checkio1_2("one two 3 four five six 7 eight 9 ten eleven 12"))
    # print(checkio1_2("123 abc abc"))
    # print(checkio1_2("one two 3 four five 6 seven eight 9 ten eleven 12"))
    # print(checkio1_2(""))

    print("Example:")
    print(checkio_2("Hello World hello"))
    print(checkio_2("bla bla bla bla"))
    print(checkio_2("He is 123 man"))
    print(checkio_2("one two 3 four five six 7 eight 9 ten eleven 12"))
    print(checkio_2('one two 3 four five 6 seven eight 9 ten eleven 12'))

    # print("Example:")
    # print(checkio_3("Hello World hello"))
    # print(checkio_3("bla bla bla bla"))
    # print(checkio_3("He is 123 man"))
    # print(checkio_3("one two 3 four five six 7 eight 9 ten eleven 12"))
    # print(checkio_3('one two 3 four five 6 seven eight 9 ten eleven 12'))
    # print(checkio_3("123 abc abc"))
    # print(checkio_3(" "))
