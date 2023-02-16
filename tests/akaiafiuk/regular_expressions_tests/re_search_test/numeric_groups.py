import re

LINE = "Some sample line with useful data. ip: 10.0.12.1  mail: sample@mail.com"

MATCH = re.search(r'ip: ([\w.]+)\s+mail: ([\w@.]+)', LINE)
# A group is defined by placing an expression in ()
# So in the expression above there are two groups:
# Group 1: ([\w.]+) - any numbers or symbols except for space, and a dot
# Group 2: ([\w.]+) - any numbers or symbols except for space, a dot and @


def test_match_entire_group():
    """.group() or .group(0) will return the entire search pattern"""
    assert MATCH.group() == 'ip: 10.0.12.1  mail: sample@mail.com'
    assert MATCH.group(0) == 'ip: 10.0.12.1  mail: sample@mail.com'


def test_match_sub_group_by_index():
    """Group numeration starts from 1
    so .group(1) will return a substring for group 1"""
    assert MATCH.group(1) == '10.0.12.1'


def test_match_sub_group_by_index_another_way():
    """Starting from python 3.6 can access sub groups using []"""
    assert MATCH[2] == 'sample@mail.com'


def test_access_multiple_sub_groups():
    """Can access multiple sub groups"""
    assert MATCH.group(2, 1) == ('sample@mail.com', '10.0.12.1')


def test_access_all_sub_groups():
    """Can access all sub groups using .groups()"""
    assert MATCH.groups() == ('10.0.12.1', 'sample@mail.com')
