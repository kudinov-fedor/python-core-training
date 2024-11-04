def chain_sum(number=0):
    total = number

    def inner(num=0):
        nonlocal total
        if num:
            total += num
            return inner
        else:
            return total
    return inner


if __name__ == "__main__":
    assert chain_sum(5)() == 5
    assert chain_sum(5)(2)() == 7
    assert chain_sum(5)(100)(-10)() == 95
