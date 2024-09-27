def sum_numbers(text: str) -> int:
    """
        Extracts numbers from the text and calculates their sum

        Args:
            text (str): text to extract numbers from

        Returns:
            int: Sum of the numbers extracted from the text
    """
    text_list = text.split()
    numbers_total = 0
    for item in text_list:
        if item.isnumeric():
            numbers_total += int(item)
    return numbers_total


def sum_numbers_comprehension(text: str) -> int:
    """
        Extracts numbers from the text and calculates their sum

        Args:
            text (str): text to extract numbers from

        Returns:
            int: Sum of the numbers extracted from the text
    """
    text_list = text.split()
    numbers_total = sum([int(item) for item in text_list if item.isnumeric()])
    return numbers_total
