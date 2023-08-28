def translate(text: str) -> str:
    vowels = "aeiouy"
    position = 0

    while position < len(text):
        if text[position] in vowels:
            text = text[:position+1] + text[position+3:]
        elif text[position] != " ":
            text = text[:position+1] + text[position+2:]
        position += 1

    return text


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    assert translate('aaa bo cy da eee fe') == 'a b c d e f'
    assert translate('sooooso aaaaaaaaa') == 'sos aaa'
    assert translate('aaa') == 'a'
    assert translate('zy') == 'z'
    assert translate('aaaeeeiiiooouuuyyy') == 'aeiouy'
