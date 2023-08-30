from typing import List


def index_power(ar: List[int], n: int) -> int:
    return ar[n]**n if n in range(len(ar)) else -1


if __name__ == "__main__":
    print("Example:")
    print(index_power([1, 2, 3], 2))

    # These "asserts" are used for self-checking
    assert index_power([1, 2, 3, 4], 2) == 9
    assert index_power([1, 3, 10, 100], 3) == 1000000
    assert index_power([0, 1], 0) == 1
    assert index_power([1, 2], 3) == -1