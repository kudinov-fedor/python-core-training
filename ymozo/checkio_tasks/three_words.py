def checkio(words: str) -> bool:
    sentences = words.split()
    words_count = 0
    for index in range(len(sentences)):
        if sentences[index].isalpha():
            words_count += 1
            if words_count >= 3:
                return True
        else:
            words_count = 0
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

    print("The mission is done! Click 'Check Solution' to earn rewards!")