def get_common_words_sol_1(first_text_row: str, second_text_row: str) -> str:
    """
        Find common words

        Args:
            first_text_row (str): text to analyze words
            second_text_row (str): text to analyze words

        Returns:
            str: words which are common in both first and second row
    """
    result = []
    first_word_list = first_text_row.split(",")
    second_word_list = second_text_row.split(",")

    for word in first_word_list:
        if word in second_word_list:
            result.append(word)

    return ",".join(sorted(result))


def get_common_words_sol_2(first_text_row: str, second_text_row: str) -> str:
    """
        Find common words

        Args:
            first_text_row (str): text to analyze words
            second_text_row (str): text to analyze words

        Returns:
            str: words which are common in both first and second row
    """

    first_word_list = first_text_row.split(",")
    second_word_list = second_text_row.split(",")

    # find common words using set intersection method
    intersection_set = set(first_word_list).intersection(set(second_word_list))

    return ",".join(sorted(intersection_set))
