def goes_after(word: str, first: str, second: str) -> bool:
    sentence = first + second
    return sentence in word


if __name__ == '__main__':
    print("Example:")
    print(goes_after("world", "w", "o"))

    # These "asserts" are used for self-checking
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after('cable', 'l', 'b') == False
    assert goes_after('cable', 'a', 'b') == True
    assert goes_after('copyrightable', 'o', 'p') == True
    assert goes_after('copyrightable', 'o', 'a') == False
    assert goes_after('copyrightable', 'o', 'o') == False
    assert goes_after('elephant', 'e', 'p') == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")