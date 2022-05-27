import pytest


@pytest.fixture(scope='module')
def get_password():
    return 'password'


@pytest.mark.parametrize("data, result",
                         [
                             ([1], 1),
                             ((1,), 1),
                             ("1", 1)
                         ],
                         ids=['list', 'tuple', 'string'])
def test_function_len_valid_data(data, result):
    assert len(data) == result


@pytest.mark.parametrize("data",
                         [1, 2.0],
                         ids=['int', 'float'])
def test_function_len_invalid_data(data):
    with pytest.raises(TypeError):
        len(data)


@pytest.mark.skip('Due to bug')
def test_password(get_password):
    password = get_password
    assert any(map(str.isdigit, password)) and not password.isdigit() is True
