import re


def translate(text: str) -> str:
    vowels = ['a', 'o', 'e', 'i', 'u', 'y']
    translated_phrase = []

    for word in text.split():
        translated_phrase.append(word)

        for index in range(0, len(word)):
            if index != len(word):
                triple_vowels = word[index + 1: index + 3] == word[index] * 2

                if word[index] in vowels and triple_vowels:
                    word = translated_phrase.pop().replace(word[index], '', 2)

                elif word[index] not in vowels and word[index + 1] in vowels:
                    chars_list = list(translated_phrase.pop())
                    del chars_list[index + 1]
                    word = ''.join(chars_list)

                translated_phrase.append(word)
            else:
                break
    return ' '.join(translated_phrase)


def translate_with_table(text: str) -> str:
    vowels = ['a', 'o', 'e', 'i', 'u', 'y']
    translated_phrase = []
    for i in vowels:
        text = text.replace(i * 3, i)

    for word in text.split():
        translated_phrase.append(word)

        for index in range(0, len(word)):
            if index != len(word):
                if word[index] not in vowels and word[index + 1] in vowels:
                    chars_list = list(translated_phrase.pop())
                    del chars_list[index + 1]
                    word = ''.join(chars_list)
                    translated_phrase.append(word)
            else:
                break

    return ' '.join(translated_phrase)


def translate_simplified(text: str) -> str:
    vowels = ['a', 'o', 'e', 'i', 'u', 'y']
    result = []
    i = 0

    while i < len(text):
        if text[i] not in vowels and text[i] != ' ':
            result.append(text[i])
            i += 2
        elif text[i] in vowels:
            result.append(text[i])
            i += 3
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)
