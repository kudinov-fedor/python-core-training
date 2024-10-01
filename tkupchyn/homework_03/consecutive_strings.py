
def consecutive_concatenation(strings: list, k: int) -> str:
    """
    Return the first longest string consisting of k consecutive strings taken in the array.

    Args:
        strings (list): list of strings
        k (int): number of consecutive strings which need to be concatenated
    Returns:
        str: longest string consisting of k consecutive strings
    """
    concatenated_strings = []

    for i in range(0, len(strings) - k + 1):
        concatenated_strings.append(''.join((strings[i: i + k])))

    return max(concatenated_strings, key=len)
