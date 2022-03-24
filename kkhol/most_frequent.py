"""You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string."""

from collections import Counter


def most_frequent(data: list) ->str:
    count = Counter(data)
    let1 = count['a']
    let2 = count['b']
    let3 = count['c']
    num = max(let1, let2, let3)
    return num
