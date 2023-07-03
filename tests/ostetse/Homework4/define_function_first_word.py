def first_word(text: str) -> str:
    """
    You are given a string, and you have to find its first word.

    The input string consists of only English letters and spaces.
    There aren’t any spaces at the beginning and the end of the string.
    Input: A string (str).

    Output: A string (str).
    """
    return text.split()[0]
