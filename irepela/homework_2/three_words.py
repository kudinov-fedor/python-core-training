def has_three_words_in_sequence(text: str) -> bool:
    """
        Checks if text has 3 words in sequence

        Args:
            text (str): text to analyze words in sequence

        Returns:
            bool: True if the text contains 3 words in sequence
    """
    word_list = text.split()
    has_three_words = False
    for index, word in enumerate(word_list):
        three_words = word_list[index: index + 3]
        has_three_words = len(three_words) == 3 and all(not word.isnumeric() for word in three_words)
        if index + 3 >= len(word_list) or has_three_words:
            break
    return has_three_words
