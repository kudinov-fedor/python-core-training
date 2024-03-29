
def chain_sum(number: int) -> callable:

    total = number

    def wrapper(number: int | None = None) -> int | callable:
        nonlocal total

        if number is None:
            return total

        total += number
        return wrapper

    return wrapper


if __name__ == "__main__":
    assert chain_sum(5)() == 5
    assert chain_sum(5)(2)() == 7
    assert chain_sum(5)(100)(-10)() == 95
