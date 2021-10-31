from textwrap import wrap


def split_pairs(a: str) -> list[str]:
    if len(a) % 2 != 0:
        a += "_"
    new_list_pairs = wrap(a, 2)
    return new_list_pairs


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))