def test_double_comparison():
    # Verify that 0 more than 5 and 5 equal 1(True)
    assert not 0 <= 5 == True
    # Verify that True expression equal True and verse
    assert (0 <= 5) == True
    assert not (0 >= 5) == True
    # Verify that 0 equal or less than False(0) etc.
    assert 0 <= (5 == True)
    assert not 1 <= (5 == True)
    assert 0 <= 5 and not 5 == True


def test_true_or_false():
    # Check one line expression <True Statement> if <Conditional Expression> else <False Statement>
    assert "it is true" == "it is true" if True else "it is false"
    assert "it is false" == "it is true" if False else "it is false"
    assert "it is false" == "it is true" if "" else "it is false"
    assert "it is true" == "it is true" if "abc" else "it is false"
    assert "it is true" != "it is true" if 0 else "it is false"
    assert "it is false" != "it is true" if 1 else "it is false"
    assert "it is true" == "it is true" if [] else "it is false"
    assert "it is true" == "it is true" if [None] else "it is false"
