#Your function should return True if the number is even, and False if the number is odd.
def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
