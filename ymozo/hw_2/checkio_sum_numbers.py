def sum_numbers(text: str) -> int:
    words_list = [0]
    splitted_string = text.split()
    for i in splitted_string:
        if i.isnumeric():
            words_list.append(int(i))
    return sum(words_list)


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers("hi"))

    # These "asserts" are used for self-checking
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
        sum_numbers(
            "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
        )
        == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0

    print("The mission is done! Click 'Check Solution' to earn rewards!")