from akaiafiuk.nearest_value import nearest_value, nearest_value_solution_two


def test_nearest_value():
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    assert nearest_value([12, 10], 11) == 10


def test_nearest_value_solution_two():
    assert nearest_value_solution_two({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value_solution_two({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value_solution_two({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value_solution_two({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value_solution_two({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value_solution_two({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value_solution_two({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value_solution_two({-1, 2, 3}, 0) == -1
    assert nearest_value([12, 10], 11) == 10
