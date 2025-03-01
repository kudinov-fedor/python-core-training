def popular_words(text: str, words_to_find: list) -> dict:
    """
    Determine the popularity of certain words in the text.

    Args:
        text (str): A text for analysis as a string.
        words_to_find(list): A list of words to find.

    Returns:
        dict: The dictionary where the search words are the keys and values are the number of times
        when those words are occurring in a given text.


    """
    list_of_words_in_lowercase = text.lower().replace('\n', ' ').split(" ")
    return {word: list_of_words_in_lowercase.count(word) for word in words_to_find}
