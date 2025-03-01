def find_common_words(string1: str, string2: str) -> str:
    """
    Finds all the words that appear in both strings

    Args:
        string1 (str): String with words separated by commas.
        string2 (str): String with words separated by commas.

    Returns:
        str: String of common words separated by commas in alphabetic order.
    """

    words = string1.split(',')
    common_words = [word for word in words if word in string2]

    return ','.join(sorted(common_words))


def common_words_alternative_solution(string1: str, string2: str) -> str:
    return ','.join(sorted(set(string1.split(',')) & set(string2.split(','))))
