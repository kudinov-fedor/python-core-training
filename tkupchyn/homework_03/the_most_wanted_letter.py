def find_most_frequent_letter(phrase: str) -> str:

    """
    Checking for the most wanted letter. If you have two or more letters with the same frequency,
    then return the letter which comes first in the Latin alphabet.
    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

    Args:
        phrase (str): A text for analysis as a string.

    Returns:
        str: The most frequent letter in lower case as a string.
    """

    phrase = [symbol.lower() for symbol in phrase if symbol.isalpha()]
    letter_frequency = {}

    for symbol in phrase:
        if symbol in letter_frequency:
            letter_frequency[symbol] += 1
        else:
            letter_frequency[symbol] = 1

    return min([elem for elem in letter_frequency if letter_frequency[elem] == max(letter_frequency.values())])
