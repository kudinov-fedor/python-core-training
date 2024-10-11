def consecutive_concatenation(strings: list, k: int) -> str:
    """
    Return the first longest string consisting of k consecutive strings taken in the array.

    Args:
        strings (list): list of strings
        k (int): number of consecutive strings which need to be concatenated
    Returns:
        str: longest string consisting of k consecutive strings
    """

    return max((''.join((strings[i: i + k])) for i in range(len(strings) - k + 1)), key=len)
