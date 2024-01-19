def test_tuple_check():
    a1 = 12,
    a2 = (12)
    a3 = (12,)

    # identity check
    assert a1 != a2
    assert a1 == a3


def test_create_dict():
    dict_var1 = dict
    dict_var2 = {}
    dict_var3 = dict()

    assert dict_var1 != dict_var2
    assert isinstance(dict_var2, dict_var1)
    assert isinstance(dict_var2, dict)
    assert dict_var1() == {}
    assert dict_var1 == dict
    assert id(dict_var1) == id(dict)
    assert dict_var2 == dict_var3
    assert dict_var1 is dict
    assert type({}) is dict


def test_create_str():
    str_var1 = str
    str_var2 = str()
    str_var3 = ''
    str_var4 = ""

    assert str_var1 != str_var2
    assert str_var2 == str_var3 == str_var4
