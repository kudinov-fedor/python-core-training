import pytest


def test_check_count():
    assert 'Please find how many a contains this text'.count('a') == 4


def test_check_find():
    assert 'Please find first s in this text'.find('s') == 4


def test_check_find_index():
    assert 'Please find first f in this text from right to left'.index('f') == 7


def test_check_find_rindex():
    assert 'From right to left'.index('f') == 16


def test_capitalize():
    assert 'nothing impossible'.capitalize() == 'Nothing impossible'


def test_split():
    assert "banana, tomatoes, apples".split(", ") == ['banana', 'tomatoes', 'apples']