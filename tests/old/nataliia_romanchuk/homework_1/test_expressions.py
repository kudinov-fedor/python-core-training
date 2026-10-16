# None True False
def test_1():
    assert int(bool(None)) == int(bool(False))
    assert int(bool(None)) == 0
    assert bool(None) == False
    assert None != False

    assert bool(True) == True
    assert int(bool(True)) == 1
    assert int(bool(True)) > 0

    assert int(bool(False)) == 0

    assert True == 1
    assert False == 0
    assert True is not 1
    assert False is not 0
    assert None != False
    assert None != 0

    assert True + True == 2
    assert True * 'ab' == 'ab'
    assert False * 10 == 0


def test_bool_numbers():
    assert bool(10) is True
    assert bool(10)
    assert bool(-2) is True
    assert bool(-2)
    assert bool(0) is False
    assert not bool(0)

    assert 0 == 0.0
    assert 0 is not 0.0
    assert bool(-3.4) is True
    assert bool(-3.4) == 1
    assert bool(-3.4) > 0

    assert 5.2 / 1 == 5.2
    assert 5.2 / 2 == 2.6
    assert 5.2 // 1 == 5.0
    assert 5.2 // 2 == 2
    assert round(5.2 % 1, 1) == 0.2
    assert round(5.2 % 2, 1) == 1.2
    assert round(5.2 % 3, 1) == 2.2

-3.4

def test_string():
    assert "abc" + "abc" == "abcabc"
    assert "abc" * 2 == "abcabc"
    assert "abcabc".islower() is True
    assert "abcabc".islower()
    assert "abcabc".isupper() is False
    assert not "abcabc".isupper()
    assert "aaabbccaa".count("a") == 5
    assert "123!".islower() is False
    assert "123!".isupper() is False
    assert "abc-123".islower()
    assert "b" in "abc"
    assert "z" not in "abc"



"""abc"""

'''abc'''

("abc"
 "def")

"abc\ndef"

"""abc
def"""

()
12, 5
(12)
(12,)

[]
[12]
[12, ]
["abc", 12.4, (), None, True]

{}
{"abc": 123}

{}
{1, 2, 3}

# ========================

bool
int
float
str
list
dict
set

bool()
int()
float()
str()
list()
dict()
set()

str.join
"".join

id(str.join)
id("".join)

str.join("|", "abc")
"|".join("abc")

str.join("|", ["a", "b", "c"])
"|".join(["a", "b", "c"])

# --------------------------

"Hello World".split(" ")[0]

a = "Hello World"
b = a.split
c = " "
d = b(c)
e = 0
f = d[e]
