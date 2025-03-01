class ObjectWithStrAndRepr(object):
    """A sample class with __repr__ and __str__ methods implemented"""

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


class ObjectWithReprOnly(object):
    """A sample class with __repr__ method implemented"""

    def __repr__(self):
        return 'repr'


def test_repr():
    """Following syntax is used to return a repr representation"""
    assert '{0!r}'.format(ObjectWithStrAndRepr()) == "repr"


def test_str():
    """Following syntax is used to return a str representation"""
    assert '{0!s}'.format(ObjectWithStrAndRepr()) == "str"


def test_str_when_only_repr_implemented():
    """__repr__ value is returned in case when __str__ representation is not implemented"""
    assert '{0!s}'.format(ObjectWithReprOnly()) == "repr"
