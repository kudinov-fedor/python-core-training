"""
You have a non-negative integer. Try to find out how many digits it has.

assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2
"""
def number_length(value: int) -> int:
    text = str(value)
    length = len(text)
    # your code here
    return length