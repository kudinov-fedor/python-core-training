'''You are given a string and you have to find its first word.'''


def first_word(text: str) -> str:
    words = text.split(' ')
    return words[0]
