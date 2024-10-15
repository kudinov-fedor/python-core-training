def popular_words(text: str, words: list) ->  dict:
    """
        Finds words occurrence in text

        Args:
            text (str): text to analyze
            words (str): list of words to find in text

        Returns:
            dict: result of words occurrence in text
    """

    result = {}
    splitted_text = text.lower().split()
    for word in words:
        result[word] = splitted_text.count(word)

    return result
