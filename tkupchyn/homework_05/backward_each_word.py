def backward_string_by_word(string: str) -> str:
    """
    Reverse every word in the given string, but the words should stay in their places.

    Args:
        string (str): list of strings
    Returns:
        str: New string with the reversed words
    """

    return ' '.join(word[::-1] for word in string.split(" "))
