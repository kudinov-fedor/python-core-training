def chain_sum(number):
    return 0


if __name__ == "__main__":
    assert chain_sum(5)() == 5
    assert chain_sum(5)(2)() == 7
    assert chain_sum(5)(100)(-10)() == 95
  
