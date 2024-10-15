def non_unique_elements(data: list[int]) -> list[int]:
    """
        Filters unique elements

        Args:
            data (str): list of integers to filter unique elements

        Returns:
            list[int]: list of non unique elements
    """
    unique_list = []
    for num in data:
        if data.count(num) == 1:
            unique_list.append(num)

    non_unique_list = [num for num in data if num not in unique_list]

    return non_unique_list
