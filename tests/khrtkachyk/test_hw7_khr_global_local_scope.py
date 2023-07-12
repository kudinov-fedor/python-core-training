import khr_hw7_global_local_scope
from khr_hw7_global_local_scope import create_global_variable, create_global_variable_2_0, add_to_global_variable, \
    use_global_variable_2_0, return_sum


def test_global_local():
    try:
        return_sum()
    except NameError:
        pass
    create_global_variable()
    assert (return_sum()) == 15
    add_to_global_variable(10)
    assert (return_sum()) == 25

    try:
        assert use_global_variable_2_0("some_key")
    except KeyError:
        pass
    create_global_variable_2_0(key="age", value=30)
    assert use_global_variable_2_0("age") == 30
    assert use_global_variable_2_0("age") != 45
