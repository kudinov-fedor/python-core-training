import re

LINE = "Some sample line with useful data. ip: 10.0.12.1  mail: sample@mail.com"

MATCH = re.search(r'ip: (?P<ip>[\w.]+)\s+mail: (?P<email>[\w@.]+)', LINE)
# A named group is defined by placing an expression in (?P<name>regex)
# So in the expression above there are two groups:
# Group 1: ([\w.]+) - any numbers or symbols except for space, and a dot
# Group 2: ([\w.]+) - any numbers or symbols except for space, a dot and @


def test_match_sub_group_by_name():
    """Group numeration starts from 1
    so .group('ip') will return a substring for group with name 'ip' """
    assert MATCH.group('ip') == '10.0.12.1'


def test_match_sub_group_by_index_another_way():
    """Starting from python 3.6 can access sub groups using []"""
    assert MATCH['email'] == 'sample@mail.com'


def test_access_multiple_sub_groups():
    """Can access multiple sub groups"""
    assert MATCH.group('email', 'ip') == ('sample@mail.com', '10.0.12.1')


def test_access_all_sub_groups():
    """Can access all sub groups using .groups()"""
    assert MATCH.groups() == ('10.0.12.1', 'sample@mail.com')


def test_get_group_dict():
    """.groupdict() allows to receive a dict with group names as dict keys and values as dict values"""
    assert MATCH.groupdict() == {'email': 'sample@mail.com', 'ip': '10.0.12.1'}
