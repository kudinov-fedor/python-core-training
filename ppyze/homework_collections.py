def first_and_last_upper_only_string(text):
    text = text[::-1].capitalize()
    text = text[0].upper() + text[::-1][1:]
    return text


def unpacking_first_and_last_only_tuple(tpl):
    a, *_, b = tpl
    return a, b


def operations_on_list(lst):
    lst += lst
    lst.append(1)
    lst *= 2
    return lst


def operations_on_set(st):
    st.add(1)
    st = st & {1,2,3,4,5}
    return st


def operations_on_dict(dc):
    dc[1] = 1
    return dc
