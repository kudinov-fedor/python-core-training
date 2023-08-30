from typing import List


def checkio(array: List[int]) -> int:
    return sum(array[::2])*array[-1] if 0 < len(array) else 0


if __name__ == "__main__":
    print("Example:")
    print(checkio([0, 1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking
    assert checkio([0, 1, 2, 3, 4, 5]) == 30
    assert checkio([1, 3, 5]) == 30
    assert checkio([6]) == 36
    assert checkio([]) == 0
    assert checkio([-89, -86, 13, -69, 94, -75, 66, 97, -50]) == -1700
    assert checkio([-78, -16, 84, 72, 33, -3, -9, -90, 13, -64, 10, -47, 99, -27, -87, -18, 76, -63]) == -8883
    assert checkio([-40, 51, -71, -12, 24, -95, 20, 8, 68, -87, 28, 89, -1, 61, 40, 56, 16, 0]) == 0
    assert checkio([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24]) == 0
    assert checkio([-5, 94, 5, -28, 17, -72, 84, 85, -17, -96, -84, -76, 0, 75]) == 0
    assert checkio([-94, 21, -58, 38, 56, 6, -91, -69, 39]) == -5772
    assert checkio([28, 54, -7, 90, 64]) == 5440
    assert checkio([39]) == 1521
    assert checkio([-37, -36, -19, -99, 29, 20, 3, -7, -64, 84, 36, 62, 26, -76, 55, -24, 84, 49, -65, 41]) == 1968
    assert checkio([43, 91, -86, 64, 25, -85, -71, -73, 23, 89, 10, 21, -78]) == 10452
    assert checkio([-36, 82, -14, 82, -59, -35, -39, 33, 28, 27, -24, 6, 83, 39, 85, 58, -44, -18, -90, -75]) == 8250
    assert checkio([69, -91, -49, -29, 13, -42, 34, -99, -97, -80, 16, -9]) == 126
    assert checkio([-43, -72, 3, -83, -82, 93, -59, -80, 6, -39, 16, 39, 1, 47, -19, 67, 51]) == -6426
    assert checkio([-80, -32, 52, -53, -21, -57, -58, -24, -15, -14, 97, -79, -35, 69]) == -4140
    assert checkio([-77, -87, -10, 98, -65, -75, -26, -46, -54, 70, -52, -81, -94, 46]) == -17388
    assert checkio([-88, 53, 55, -74, -36, 20, 95, -22, -63, -53, -68]) == 7140
    assert checkio([45]) == 2025
    assert checkio([72, -19, -73, -59, 83, -79, -90]) == 720

    print("The mission is done! Click 'Check Solution' to earn rewards!")
