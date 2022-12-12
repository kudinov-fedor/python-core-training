from collections import Counter
from typing import List


def most_frequent(letters: List[str]) -> str:
    return Counter(letters).most_common(1)[0][0]


def most_frequent_with_max(data: List[str]):
    return max(set(data), key=data.count)
