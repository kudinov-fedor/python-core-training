from akaiafiuk.end_zeros import end_zeros, end_zeros_using_split, end_zeros_using_zip, end_zeros_using_generator, \
    end_zeros_using_translate


def test_end_zeros():
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    assert end_zeros(1234567890000) == 4


def test_end_zeros_using_split():
    assert end_zeros_using_split(0) == 1
    assert end_zeros_using_split(1) == 0
    assert end_zeros_using_split(10) == 1
    assert end_zeros_using_split(101) == 0
    assert end_zeros_using_split(245) == 0
    assert end_zeros_using_split(100100) == 2
    assert end_zeros(1234567890000) == 4


def test_end_zeros_using_zip():
    assert end_zeros_using_zip(0) == 1
    assert end_zeros_using_zip(1) == 0
    assert end_zeros_using_zip(10) == 1
    assert end_zeros_using_zip(101) == 0
    assert end_zeros_using_zip(245) == 0
    assert end_zeros_using_zip(100100) == 2
    assert end_zeros_using_zip(1234567890000) == 4


def test_end_zeros_using_generator():
    assert end_zeros_using_generator(0) == 1
    assert end_zeros_using_generator(1) == 0
    assert end_zeros_using_generator(10) == 1
    assert end_zeros_using_generator(101) == 0
    assert end_zeros_using_generator(245) == 0
    assert end_zeros_using_generator(100100) == 2
    assert end_zeros_using_generator(1234567890000) == 4


def test_end_zeros_using_translate():
    assert end_zeros_using_translate(0) == 1
    assert end_zeros_using_translate(1) == 0
    assert end_zeros_using_translate(10) == 1
    assert end_zeros_using_translate(101) == 0
    assert end_zeros_using_translate(245) == 0
    assert end_zeros_using_translate(100100) == 2
    assert end_zeros_using_translate(1234567890000) == 4
