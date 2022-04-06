"""You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string."""

from collections import Counter

data = 'a, b, c, a, b, a'


def most_frequent(data: list) -> int:
    # count = Counter(data)
    let1 = data.count('a')
    let2 = data.count('b')
    let3 = data.count('c')
    num = max(let1, let2, let3)
    return num

print(most_frequent(data))
