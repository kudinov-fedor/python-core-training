import pytest


@pytest.mark.parametrize("str1, val1, exp", [
    (" hello, and welcome to the python!", 2, " hello, and welcome to the python! hello, and welcome to the python!" ),
    ("Privet", 3, "PrivetPrivetPrivet"),
    (4, 8, 32)
])
def test_multiply(str1, val1, exp):
        assert str1 * val1 == exp


@pytest.mark.parametrize("str1, str2, ", [
    ("hello, and welcome to the python!", "hello"),
    ("hello, and welcome to the python!", "to")
])
def test_contains(str1, str2):
    assert str1.__contains__(str2) == True


def test_not_contains():
    string1 = "hello, and welcome to the python!"
    assert not string1.__contains__('foo') == True


@pytest.mark.parametrize("str1, str2", [
    ("hello, and welcome to the python!", 'hello'),
    ('Hello', 'o'),
    ('1234', '3')
])
def test_contains2(str1, str2):
        assert str2 in str1


@pytest.mark.parametrize("str1, str2", [
    ("hello, and welcome to the python!", 'hello3'),
    ('Hello', 'o2'),
    ('1234', '32')
])
def test_not_contains2(str1, str2):
        assert not str2 in str1


def test_assertTrue2():
    a = 9
    b = 5
    assert (a > b) == True


def test_assertTrue3():
    assert True


def test_assertTrue4():
    assert 125


def test_assertTrue5():
    assert "Fooo"


def test_assertFalse():
    a = 9
    b = 5
    assert (b > a) == False


def test_assertFalse1():
    assert "" == ""


def test_assertFalse2():
    assert 0 == False




################### String methods #################

@pytest.mark.parametrize("str1, exp", [
    ("hello, and welcome to the python!", "Hello, and welcome to the python!"),
    ('hello', 'Hello'),
    ('kids', 'Kids')
])
def test_capitalize(str1, exp):
        assert str1.capitalize() == exp

@pytest.mark.parametrize('str1, str2', [
    ('Hello, And Welcome To the Python!', 'hello, and welcome to the python!'),
    ('Hello, Allo, AllLLo, PYTHON', 'hello, allo, allllo, python')
])
def test_casefold(str1, str2):
        assert str1.casefold() == str2


@pytest.mark.parametrize('str1, str2, start, fin, exp', [
    ('I love apples, apple are my favorite fruit', 'apple', 1, 100, 2),
    ('I love apples, apple are my favorite fruit', 'apple', 10, 100, 1),
    ('I love apples, apple are my favorite fruit, apple', 'apple', 1, 100, 3)
])
def test_count(str1, str2, start, fin, exp):
        assert str1.count(str2, start, fin) == exp


@pytest.mark.parametrize('str1, exp', [
    ("I love Python", b'I love Python'),
    ("I I love Python I", b'I I love Python I')
])
def test_encode(str1, exp):
         assert str1.encode() == exp


@pytest.mark.parametrize('str1, letter1', [
    ('i Python', 'n'),
    ('I love', 'e'),
    ('testing', 'g')
])
def test_endswith(str1, letter1):
        assert str1.endswith(letter1)


@pytest.mark.parametrize("str1, letter1, start, end", [
    ('Python, python', ' ', 1, 8),
    ('Python, python', 'n', 7, 77),
    ('Pnnnython, python', 'n', 1, 3)
])
def test_endswith2(str1, letter1, start, end):
        assert str1.endswith(letter1, start, end)




@pytest.mark.parametrize("data, val, start_position, end_position, expected", [
    ("I love Python", "o", 5, 20, 11),
    ("I love Python", "o", 0, 20, 3),
    ("I love Python", "r", 3, 5, -1),
    ("I love Python", "er", 10, 15, -1)
])
def test_find(data, val, start_position, end_position, expected):
    assert data.find(val, start_position, end_position) == expected

@pytest.mark.parametrize("val1, val2, exp", [
    ("I love Python", " so much", "I love Python so much")
])
def test_operatorPlus(val1, val2, exp):
        assert val1 + val2 == exp

@pytest.mark.parametrize("val1, val2, exp", [
    (3, 5, 15),
    (4, 10, 40),
    (9, 11, 99)
])
def test_operatorMultiply(val1, val2, exp):
        assert val1 * val2 == exp


@pytest.mark.parametrize("val1, val2", [
    (4, 1,),
    (10, 5,)
])
def test_operatorMore(val1, val2,):
    assert val1 > val2


@pytest.mark.parametrize('val1, val2', [
    (9, 11),
    (7, 16)
])
def test_operatorLess(val1, val2):
    assert val1 < val2


@pytest.mark.parametrize('val1, val2', [
    (9, 9),
    (9, 12)
])
def test_operatorLessEqual(val1, val2):
    assert val1 <= val2


@pytest.mark.parametrize('str1, str2', [
    ("string", "string1"),
    ('str12', 'str21'),
    (9, 91)
])
def test_operatorNotEqual(str1, str2):
    assert str1 != str2



@pytest.mark.parametrize('iterab, separator, exp', [
    ({"name": "Viktor", "city": "Odessa"}.values(), ' love ', "Viktor love Odessa"),
    ({'name': 'Python', 'lang': 'Python'}.values(), ' equal ', 'Python equal Python'),
    ['pyton', 'equal', 'pequalyequaltequaloequaln'],
    [('pyton', 'language'), 'join', 'pytonjoinlanguage']
])
def test_join(iterab, separator, exp):
        assert separator.join(iterab) == exp


@pytest.mark.parametrize("str1, exclude, exp", [
    (" ccccccc I love Python and Odessa ,....,..vvvv"," c,.v", "I love Python and Odessa" ),
    (" qqqcc I love Python and Odessa ,....,..vvvv"," c,.vq", "I love Python and Odessa" ),
    ["qqqcc I love Python and Odessa ,....,..vvvv"," c,.vq", "I love Python and Odessa"]
])
def test_strip(str1, exclude, exp):
        assert str1.strip(exclude) == exp


@pytest.mark.parametrize('str1, args, exp', [
    ("I love Python and Odessa ! ", (' ', 2), ['I', 'love', 'Python and Odessa ! ']),
    ("I love Python and Odessa ! ", (' ', 3), ['I', 'love', 'Python', 'and Odessa ! ']),
    ("I love Python and Odessa ! ", (" ",), ['I', 'love', 'Python', 'and', 'Odessa', '!', ''])
])
def test_split(str1, args, exp):
        assert str1.split(*args) == exp
        print((str1.split(*args)))


@pytest.mark.parametrize('str1, sep, exp',[
    ("I love Python and Odessa ! ", ' ', ['I', 'love', 'Python', 'and', 'Odessa', '!', '']),
    ("I, love, Python and Odessa ! ", ', ', ['I', 'love', 'Python and Odessa ! ']),
    ])
def test_splitComa(str1, sep, exp):
        assert str1.split(sep) == exp



@pytest.mark.parametrize('str1, args, exp', [
    ["I love love love Python and also love Odessa ! ", ('love','LOVE',2), "I LOVE LOVE love Python and also love Odessa ! " ],
    ["I love love Python love and also love Odessa ! ", ('love','LOVE',3), "I LOVE LOVE Python LOVE and also love Odessa ! " ],
    ("I love love Python love and also love Odessa ! ", ('love','LOVE',2), "I LOVE LOVE Python love and also love Odessa ! " ),
    ("I love love Python love and also love Odessa ! ", ('love','LOVE',), "I LOVE LOVE Python LOVE and also LOVE Odessa ! " )
])
def test_replace1(str1, args, exp):
        assert str1.replace(*args) == exp

