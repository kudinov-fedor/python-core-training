"""
****** Task1 ********************************************************
Backward String
*********************************************************************
"""


def backward_string(val: str) -> str:
    return ''.join(reversed(val))


# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"


def backward_string2(val: str) -> str:
    return val[::-1]


# These "asserts" are used for self-checking
assert backward_string2("val") == "lav"
assert backward_string2("") == ""
assert backward_string2("ohho") == "ohho"
assert backward_string2("123456789") == "987654321"