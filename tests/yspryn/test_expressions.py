def test_tuple_check():
    a1 = 12,
    a2 = (12)
    a3 = (12,)

    # identity check
    assert a1 != a2
    assert a1 == a3

def test_create_check():
    dict_var1 = dict
    dict_var2 = {}
    dict_var3 = dict()

    assert dict_var1 != dict_var2
    assert dict_var2 == dict_var3

    str_var1 = str
    str_var2 = str()
    str_var3 = ''
    str_var4 = ""

    assert str_var1 != str_var2
    assert str_var2 == str_var3 == str_var4
