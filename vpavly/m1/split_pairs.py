"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.
"""


# def split_pairs(a: str) -> list:
#     a += '_' if len(a) % 2 else a
#     b = []
#     for i in range(0, len(a) - 1, 2):
#         b.append(a[i] + a[i + 1])
#     return b


def split_pairs(a: str) -> list:
    b = a + '_' if len(a) % 2 else a
    result = []
    for i in (item for item in zip(b[::2], b[1::2])):
        result.append(i[0] + i[1])
    return result
