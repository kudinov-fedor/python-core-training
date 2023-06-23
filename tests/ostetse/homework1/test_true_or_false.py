import pytest


def test_conversion_to_boolean():
    assert all([
        bool(True),
        bool(3),
        bool(-0.1),
        bool("abc"),
        bool([False, ]),
        bool((None,)),
        bool({"a": 123}),
        bool({1, "abc"})
    ])


def test_comparison():
    assert "it is true" if True else "it is false" == "it is true"
    assert "it is true" if False else "it is false" == "it is false"
    assert "it is true" if "" else "it is false" == "it is false"
    assert "it is true" if "abc" else "it is false" == "it is true"
    assert "it is true" if 0 else "it is false" == "it is false"
    assert "it is true" if 1 else "it is false" == "it is true"
    assert "it is true" if [] else "it is false" == "it is false"
    assert "it is true" if [None] else "it is false" == "it is false"



