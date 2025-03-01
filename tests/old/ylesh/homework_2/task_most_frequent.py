"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
It can be the only one.
"""


def most_frequent(data: list[str]) -> str:
    return max(set(data), key=data.count)


assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
