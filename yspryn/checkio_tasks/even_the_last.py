# You are given list of integers (int).
# You should find the sum of the elements with even indexes (0th, 2nd, 4th...).
# Then multiply this summed number and the final element of the list together.
# Don't forget that the first element has an index of 0.
# For an empty list, the result will always be 0 (zero).

def even_the_last(array: list[int]) -> int:
    res = 0
    for i in range(len(array)):
        if i % 2 == 0:
            res += array[i]
    if res:
        res *= array[-1]
    print(res)
    return res


def even_the_last2(array: list[int]) -> int:
    res = 0
    for i in array[::2]:
        res += i
    if res:
        res *= array[-1]
    return res
