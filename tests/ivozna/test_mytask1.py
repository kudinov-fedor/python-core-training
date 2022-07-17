from ivozna.my_task1 import first_word

def test_mytask1():
    res = first_word('Hi World')
    assert first_word('Hi') == 'Hi'
