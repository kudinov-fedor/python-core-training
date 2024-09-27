def has_three_words_in_sequence_sol_1(text: str) -> bool:
    """
        Checks if text has 3 words in sequence

        Args:
            text (str): text to analyze words in sequence

        Returns:
            bool: True if the text contains 3 words in sequence
    """
    counter = 0
    word_list = text.split()

    for word in word_list:

        if word.isnumeric():
            counter = 0
        else:
            counter += 1

        if counter == 3:
            break

    return counter == 3


def has_three_words_in_sequence_sol_2(text: str) -> bool:
    """
        Checks if text has 3 words in sequence

        Args:
            text (str): text to analyze words in sequence

        Returns:
            bool: True if the text contains 3 words in sequence
    """
    word_list = text.split()
    has_three_words = False
    for index in range(len(word_list) - 2):
        three_words = word_list[index: index + 3]
        has_three_words = all(not word.isnumeric() for word in three_words)
        if has_three_words:
            break
    return has_three_words
