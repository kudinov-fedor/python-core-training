def sum_numbers(string) -> int:
    """
        Sums all the integers present in the input string.

        The function splits the input string into words, checks if each word is a digit,
        and sums all valid integers. Non-digit words are ignored.

        Args:
        string (str): A string containing words and/or numbers separated by spaces.

        Returns:
        int: The sum of all integers found in the input string. If no integers are found, returns 0.
        """
    return sum(int(num) for num in string.split() if num.isdigit())
