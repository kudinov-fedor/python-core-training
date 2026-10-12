#########################
# conversion to Boolean #
#########################
from logging import log

from tests.old.kkhol.builtins_practice import eq


def test_false():
    assert bool(None) is False
    assert bool({}) is False
    assert bool([]) is False
    assert bool({}) == 0
    assert bool([]) == 0
    assert bool(None) == 0
    assert bool("") is False
    assert bool([]) == 0
    assert bool(set()) == 0


def test_bool_false():
    assert bool(False) is False
    assert bool(False) == 0
    assert int(bool(False)) == 0
    assert bool(0) is False
    assert bool(0.0) is False

def test_bool_class():
    assert bool(bool()) is False
    assert bool(int()) is False
    assert bool(float()) is False
    assert bool(str()) is False
    assert bool(tuple()) is False
    assert bool(dict()) is False
    assert bool(set()) is False
    assert bool(list()) is False

def test_bool_true():
    assert bool(True) is True
    assert bool(3) is True
    assert bool(-0.1) is True
    assert bool(-0.1) > 0
    assert int(bool(-0.1)) == 1
    assert bool(-0.1) == 1
    assert bool(1) is True

# containers bool check
def test_container_true():
    assert bool("cat") is True
    assert bool("dog") is True
    assert bool([False, ]) is True
    assert bool([None, ]) is True
    assert bool({'a': 123}) is True

def test_containers_len():
    assert len("cat") > 0
    assert bool(len("dog")) is True
    assert len([False, ]) > 0
    assert len([None, ]) == 1
    assert len((None, )) > 0
    assert len((None,)) == 1


def test_not():
    assert not 5 is False
    assert not 0 is True
    assert not True is False
    assert not False is True
    assert not [] is True
    assert not (1,2,3) is True
    assert not ((1,2,3)  is True) is True
    assert not (1,2,3) is False
    assert not ((1,2,3) is False) is True

    res1=not (1,2,3) is True
    res2=not (1,2,3) is False
    res3=not ((1,2,3) is True) is True
    res4=not ((1,2,3) is False) is True
    assert res1 == res2 == res3 == res4 == True



# comparison
"it is true" if True else "it is false"
"it is true" if False else "it is false"
"it is true" if "" else "it is false"
"it is true" if "abc" else "it is false"
"it is true" if 0 else "it is false"
"it is true" if 1 else "it is false"
"it is true" if [] else "it is false"
"it is true" if [None] else "it is false"


# take first True item, or last
True or False
False or True
1 or 3
[] or "abc"
None or "some"
None or 0 or "" or [] or "at last some value"
None or 0 or "" or [] or {}

# take first False item, or last
True and False
False and True
1 and 3
[1, 2, 3] and "abc"
"some" and {}
1 and "abc" and 0.0 and "some value"

# priority is important
"" or "Some" and {}
"" or "Some" and {}
False or "" and 123
False or "" and 123


# if all are true
def test_all_is_true():
    assert all(["a", 0, True, (1, 2, 3)]) is False
    assert all(["a", -1, True, (1, 2, 3)]) is True
    assert all(["a", -1, False, (1, 2, 3)]) is False
    assert all(["a", -1, True, ()]) is False

# if at least 1 is true
def test_any_one_is_true():
    assert any(["", 0, False, (), None]) is False
    assert any(["", 1, False, (), None]) is True
    assert any(["", 0, True, (), None]) is True
    assert any(["", 0, False, (1,), None]) is True


# filter by default leaves only true elements,
# but you can specify other logic

data = ["cat", "dog", "", None, False, 0, 1, -2, True]
list(filter(None, data))
list(filter(lambda i: isinstance(i, str), data))


