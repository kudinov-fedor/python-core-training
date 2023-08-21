def checkio(words: str) -> bool:
    sentence = words.split()
    for index in range(len(sentence) - 2):
        word1 = sentence[index]
        word2 = sentence[index + 1]
        word3 = sentence[index + 2]

        if word1.isalpha() and word2.isalpha() and word3.isalpha():
            return True

    return False


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World hello"))

    # These "asserts" are used for self-checking
    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False
    assert checkio("12 12 12 Bla bla bla")

    print("The mission is done! Click 'Check Solution' to earn rewards!")