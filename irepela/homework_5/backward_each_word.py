def backward_each_word(text: str) -> str:
    """
        Reverses each word in given string

        Args:
            text (str): string to reverse word in

        Returns:
            str: string with reversed words
    """

    return " ".join([word[::-1] for word in text.split(" ")])
