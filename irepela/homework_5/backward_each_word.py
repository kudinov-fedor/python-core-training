def backward_each_word(text: str) -> str:
    """
        Reverses each word in given string

        Args:
            text (str): string to reverse word in

        Returns:
            str: string with reversed words
    """
    word_list = text.split(" ")
    reversed_word_list = []
    if len(word_list) == 1:
        reversed_word_list.append(text[::-1])
    else:
        for word in word_list:
            reversed_word_list.append(word[::-1])

    return " ".join(reversed_word_list)