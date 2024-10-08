from string import ascii_lowercase


def get_most_wanted_letter(text: str) -> str:
    """
        Find most used letter

        Args:
            text (str): text to analyze letters usage

        Returns:
            str: letter which is used the most
    """

    text = text.lower()

    return max(ascii_lowercase, key=text.count)
