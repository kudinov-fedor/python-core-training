
class ObjectWithFormatDefined:

    def __format__(self, format_spec: str) -> str:
        if format_spec == 'hex':
            return '2A'
        if format_spec == 'bin':
            return '101010'
        return '42'

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


def test_formatting_bin():
    assert "{:bin}".format(ObjectWithFormatDefined()) == '101010'


def test_formatting_other():
    assert "{}".format(ObjectWithFormatDefined()) == '42'


def test_format_str():
    assert '{0!s}'.format(ObjectWithFormatDefined()) == "str"


def test_format_str():
    assert '{0!r}'.format(ObjectWithFormatDefined()) == "repr"
