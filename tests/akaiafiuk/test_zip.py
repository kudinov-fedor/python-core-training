import pytest


@pytest.mark.xfail
def test_zip_type():
    """Verify that zip() returns an object of zip type"""
    assert isinstance(zip(), zip)


@pytest.mark.my_mark
@pytest.mark.parametrize('input_one, input_two, expected_result', [
    ([1, 2, 3], ['a', 'b', 'c'], [(1, 'a'), (2, 'b'), (3, 'c')]),
    ([1, 2, 3], ('a', 'b', 'c'), [(1, 'a'), (2, 'b'), (3, 'c')]),
    ([1, 2, 3], 'abc', [(1, 'a'), (2, 'b'), (3, 'c')]),
])
def test_zip_with_various_data_types(input_one, input_two, expected_result):
    """Verify that various data types could be zipped"""
    assert list(zip(input_one, input_two)) == expected_result


def test_zip_as_iterator():
    """Testing zip as iterator"""
    input_one = [1, 2, 3]
    input_two = ['a', 'b', 'c']
    zipped = zip(input_one, input_two)
    for i in range(len(input_one)):
        assert next(zipped) == (input_one[i], input_two[i])


def test_zip_unequal_len():
    """Verify that zipped object has a length of the shortest input"""
    assert len(list(zip(range(5), range(100)))) == 5
