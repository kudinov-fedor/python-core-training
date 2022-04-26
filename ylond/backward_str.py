# You should return a given string in reverse order

def backward_string(text: str) -> str:
    my_str = list(reversed(text))
    my_lst_str = ''.join(map(str, my_str))
    return my_lst_str

