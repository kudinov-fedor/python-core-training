"""
****** Task1 ********************************************************
Backward String
*********************************************************************
"""


def backward_string(val: str) -> str:
    chars_list = []
    new_str = ''
    for char in val:
        chars_list.append(char)
    for char in chars_list.__reversed__():
        new_str += char
    return new_str


# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"
