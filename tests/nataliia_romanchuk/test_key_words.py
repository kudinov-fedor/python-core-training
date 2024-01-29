def test_not():
    assert not (1 == 11)
    assert not (1 == '11')
    assert not (1 == '1')
    assert not (11 == '1' + '1')
    assert not (11 == '10' + '1')
    assert not (1 == None)
    assert not (1 == False)


def test_and():
    assert (1 == 1) and ('1' == '1')
    assert not ((1 == 1) and ('1' == 1))


def test_or():
    assert (1 == 1) or (1 == '1')
    assert not (1 == 1) or ('1' == '1')
    assert "abc" and "def" == "def"
    assert ("" and "def") == ""


def test_in():
    assert 1 in [1, 11, 111]
    assert 'a' in 'cat'


def test_is():
    a = [1, 11, 111]
    b = a
    assert a is b


def test_is_not():
    a = [1, 11, 111]
    b = [2, 22, 222]
    assert a is not b


def test_not_in():
    assert 0 not in [1, 11, 111]
    assert 'sausage' not in 'cat'


def test_if_else():
    x = 1
    if x > 0:
        pass
    else:
        raise AssertionError
    assert x > 0


def test_for_in():
    array = [1, 10, 100, 1000]
    sum = 0
    for element in array:
        sum += element
    assert sum == 1111


def test_while():
    x = 0
    while x < 5:
        x += 1
    assert x == 5


def test_list_comprehension():
    numbers = [1, 11, 111]
    squares = [x ** 2 for x in numbers]
    assert squares == [1, 11 ** 2, 111 ** 2]


def test_dict_comprehension():
    keys = range(1, 4)
    values = [1, 11, 111]
    my_dict = {key: value for key, value in zip(keys, values)}
    square_dict = {key: value ** 2 for key, value in my_dict.items()}
    expected_square_dict = {1: 1, 2: 11 ** 2, 3: 111 ** 2}
    assert square_dict == expected_square_dict


def test_set_comprehension():
    numbers = [1, 11, 111]
    squares_set = {num ** 2 for num in numbers}
    assert squares_set == {1, 121, 12321}


def test_generator_expression():
    numbers = [1, 2, 3]
    square_generator = (num ** 2 for num in numbers)
    assert list(square_generator) == [1, 4, 9]
