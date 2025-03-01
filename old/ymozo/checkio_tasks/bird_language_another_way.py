import random


def translate_birds(text: str) -> str:
    vowels = "aeiouy"
    translated = ""
    index = 0

    while index < len(text):
        translated += text[index]
        if text[index] == " ":
            index += 1
        elif text[index] not in vowels:
            index += 2
        else:
            index += 3
    return translated


if __name__ == "__main__":
    print("Example:")
    print(translate_birds("hieeelalaooo"))
    assert translate_birds("hieeelalaooo") == "hello"
    assert translate_birds("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate_birds("aaa bo cy da eee fe") == "a b c d e f"
    assert translate_birds("sooooso aaaaaaaaa") == "sos aaa"
    assert translate_birds('aaa bo cy da eee fe') == 'a b c d e f'
    assert translate_birds('sooooso aaaaaaaaa') == 'sos aaa'
    assert translate_birds('aaa') == 'a'
    assert translate_birds('zy') == 'z'
    assert translate_birds('aaaeeeiiiooouuuyyy') == 'aeiouy'
