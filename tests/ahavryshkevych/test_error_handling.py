import pytest

from ahavryshkevych.task_exceptions import key_error, index_error, name_error, attribute_error, \
    assertion_error, type_error


def test_type_error():
    with pytest.raises(TypeError):
        type_error()


def test_key_error():
    try:
        key_error()
    except KeyError:
        pass


def test_index_error():
    try:
        index_error()
    except IndexError:
        pass
    finally:
        print(f"there is potential error tht was missed {IndexError}")


def test_name_error():
    with pytest.raises(NameError):
        name_error(a)


def test_attribute_error():
    try:
        attribute_error()
    except ZeroDivisionError:
        pass
    else:
        print("this error {} didn't happened".format(ZeroDivisionError))
    finally:
        print("The end")


def test_assertion_error():
    try:
        assertion_error()
    except Exception as error:
        print(error)
