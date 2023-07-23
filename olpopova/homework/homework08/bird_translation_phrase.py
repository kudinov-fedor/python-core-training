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
    translation_table = {vowels[0] * 3: vowels[0],
                         vowels[1] * 3: vowels[1],
                         vowels[2] * 3: vowels[2],
                         vowels[3] * 3: vowels[3],
                         vowels[4] * 3: vowels[4],
                         vowels[5] * 3: vowels[5],
                         }
    translated_with_table = custom_make_translation(text, translation_table)

    for word in translated_with_table.split():
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


def custom_make_translation(text, translation):
    regex = re.compile('|'.join(map(re.escape, translation)))
    return regex.sub(lambda match: translation[match.group(0)], text)


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
