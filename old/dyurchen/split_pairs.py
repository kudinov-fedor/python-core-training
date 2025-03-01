def split_pairs(a: str) -> list:
    if len(a) % 2 != 0:
        a += "_"
    return [a[i: i + 2] for i in range(0, len(a), 2)]
