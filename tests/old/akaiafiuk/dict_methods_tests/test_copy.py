def test_copy(default_dict):
    """copy() method returns a copy of the dict. This is a new object"""
    some_other_dict = default_dict.copy()
    assert some_other_dict == default_dict
    assert some_other_dict is not default_dict


def test_assignment(default_dict):
    """when you create a copy using assignment the object remains the same"""
    some_other_dict = default_dict
    assert some_other_dict == default_dict
    assert some_other_dict is default_dict


def test_difference_between_copy_and_assignment(default_dict):
    """test side effect that copy helps to get around"""
    some_dict_assigned = default_dict
    some_dict_copy = default_dict.copy()
    default_dict[1] = 'ONE'
    assert some_dict_assigned[1] == 'ONE'
    assert some_dict_copy[1] == 'one'
