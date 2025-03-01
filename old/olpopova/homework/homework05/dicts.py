from collections import defaultdict
from typing import List, Dict


def group_by(data: List[dict], key: str) -> Dict[str, list]:
    """
    group items from list into dict
    where key is a value from parameter provided as key parameter
    Usage example:
    data = [{"a": "1", "b": 1}, {"a": "1", "b": 2}, {"a": "2", "b":3}]
    assert group_by(data, "a") == {
        "1": [{"a": "1", "b": 1}, {"a": "1", "b": 2}],
        "2": [{"a": "2", "b":3}]
    }
    """
    by_key = defaultdict(list)
    for i in data:
        by_key[i[key]].append(i)

    return by_key
