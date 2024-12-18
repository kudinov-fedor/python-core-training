import pytest
from tkupchyn.homework_06.min_max_sorted import custom_min, custom_max, custom_sorted


def test_custom_min():
    assert custom_min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert custom_min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def test_custom_max():
    assert custom_max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert custom_max(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == -7


def test_custom_sorted():
    assert custom_sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert custom_sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert custom_sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert custom_sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
