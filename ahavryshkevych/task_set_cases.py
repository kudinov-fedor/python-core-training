def set_equality01(arg1, arg2):
    return arg1 == arg2


def set_equality02(arg1, arg2):
    return arg1 < arg2


def set_union(set1, set2):
    return len(set1 | set2) == len(set1) + len(set2)


def set_difference(set1, set2):
    return set1.difference(set2)
