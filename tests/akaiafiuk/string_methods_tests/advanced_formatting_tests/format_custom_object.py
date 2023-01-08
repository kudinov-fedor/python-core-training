
class ObjectWithFormatDefined:

    def __format__(self, format_spec: str) -> str:
        if format_spec == 'hex':
            return '2A'
        if format_spec == 'bin':
            return '101010'
        return '42'


def test_formatting_bin():
    assert "{:bin}".format(ObjectWithFormatDefined()) == '101010'


def test_formatting_other():
    assert "{}".format(ObjectWithFormatDefined()) == '42'
