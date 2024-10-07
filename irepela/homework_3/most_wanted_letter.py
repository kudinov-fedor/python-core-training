def get_most_wanted_letter(text: str) -> str:
    """
        Find most used letter

        Args:
            text (str): text to analyze letters usage

        Returns:
            str: letter which is used the most
    """

    # lowercase all text, remove non alpha strings and sort it alphabetically
    text = "".join(letter for letter in sorted(text.lower()) if letter.isalpha())

    # calculate letter max occurrence
    max_value_letter = max(text, key=text.count)

    return max_value_letter
