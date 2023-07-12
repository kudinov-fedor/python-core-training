import pytest

import khr_hw7_global_local_scope
from khr_hw7_global_local_scope import (create_global_variable, create_global_variable_2_0,
                                        add_to_global_variable, use_global_variable_2_0, return_sum)


def test_global_local():
    with pytest.raises(NameError):
        return_sum()
    create_global_variable()
    assert (return_sum()) == 15
    add_to_global_variable(10)
    assert (return_sum()) == 25

    with pytest.raises(KeyError):
        use_global_variable_2_0("some_key")
    create_global_variable_2_0(key="age", value=30)
    assert use_global_variable_2_0("age") == 30
    assert use_global_variable_2_0("age") != 45
    assert khr_hw7_global_local_scope.age == 30
    assert hasattr(khr_hw7_global_local_scope, "age")
    assert getattr(khr_hw7_global_local_scope, "age") == 30
