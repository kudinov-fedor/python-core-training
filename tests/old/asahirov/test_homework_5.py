import pytest


@pytest.mark.parametrize(
    "group_key, group_value_1, group_value_2, group_len_1, group_len_2",
    [
        ("name", "Marry", "John", 2, 1),
        ("sex", "M", "F", 2, 2),
        ("age", 16, 34, 1, 3)
    ]
)
def test_dicts(
        group_key,
        group_value_1,
        group_value_2,
        group_len_1,
        group_len_2
):
    """Group data by key and verify length"""
    data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
            {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
            {"age": 34, "second_name": "Katon", "name": "Marry", "sex": "F"},
            {"age": 34, "second_name": "Maton", "name": "Mathew", "sex": "M"}]

    grouped_dict = {}
    for i in data:
        grouped_dict.setdefault(i[group_key], []).append(i)

    assert group_len_1 == len(grouped_dict[group_value_1])
    assert group_len_2 == len(grouped_dict[group_value_2])


def test_sets():
    some_set = {"a", "b", "c"}
    some_set_2 = {"b", "a", "c"}
    assert some_set.issuperset({"a", "c"})
    assert some_set_2.issuperset(["c", "c"])
    assert not some_set.issuperset(["ac"])

    union_set = {"a", "b", "x"}.union({"a", "x", "f"})
    assert len(union_set) == 4
    union_set.update(some_set_2)
    assert len(union_set) == 5
