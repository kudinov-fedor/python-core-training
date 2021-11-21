"""
You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.
"""


def even_last(numbers: list) -> int:
    return (sum([numbers[even_index] for even_index in range(len(numbers)) if even_index % 2 == 0]) * numbers[-1]) if numbers else 0
