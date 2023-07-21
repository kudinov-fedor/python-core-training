
name = "something"


def change_global_var():
    global name
    name = 'Pfirsik'
    return name


def change_local():
    name = 'other_value'
    return name


def get_global_value():
    global name
    return name


def test_change_global():
    assert get_global_value() == 'something'
    assert change_global_var() == 'Pfirsik'
    assert change_local() != name
    assert get_global_value() == 'Pfirsik'


