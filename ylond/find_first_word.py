# find first word (without spaces in the start)


def first_word(text: str) -> str:
    result = text.split(" ")
    return result[0]
