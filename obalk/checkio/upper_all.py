def all_upper(text: str) -> bool:
    return not any(letter.islower() for letter in text)


def all_upper_upper(text: str) -> bool:
    return text.upper() == text
