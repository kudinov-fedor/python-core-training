def non_unique_elements(data: list[int]) -> list[int]:
    """
        Filters unique elements

        Args:
            data (str): list of integers to filter unique elements

        Returns:
            list[int]: list of non unique elements
    """
    return [num for num in data if data.count(num) > 1]
