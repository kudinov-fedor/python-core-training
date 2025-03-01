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
