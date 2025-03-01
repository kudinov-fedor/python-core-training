def three_in_row(text: str) -> bool:
    """
    Checks if the string contains three words in succession.

    Args:
    text (str): The input string that may contain a mixture of words and non-word elements.

    Returns:
    bool: True if there are three in succession, False otherwise.
    """

    count = 0
    for elem in text.split():

        if not elem.isdigit():
            count += 1
        else:
            count = 0

        if count == 3:
            return True

    return False


def three_in_row_alternative_solution(text: str) -> bool:
    """
    Checks if the string contains three words in succession.

    Args:
    text (str): The input string that may contain a mixture of words and non-word elements.

    Returns:
    bool: True if there are three in succession, False otherwise.
    """

    words = text.split()

    for i in range(len(words) - 2):
        three_words = words[i: i + 3]
        if all(word.isalpha() for word in three_words):
            return True

    return False
