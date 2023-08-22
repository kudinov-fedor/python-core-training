def checkio(text: str) -> str:
    storage = []

    for letter in sorted(text.lower()):
        if letter.isalpha():
            storage.append(letter)

    return max(storage, key=storage.count)


if __name__ == "__main__":
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" are used for self-checking
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"

    print("The mission is done! Click 'Check Solution' to earn rewards!")