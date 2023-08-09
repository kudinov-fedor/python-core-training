from olpopova.homework.homework09.fraction import Fraction


def test_str_repr():
    a = Fraction(2, 4)
    assert repr(a) == "Fraction(1, 2)"
    assert str(a) == "'1 / 2'"
    assert "val: {:dec}".format(a) == "val: 0.5"
    assert "val: {}".format(a) == "val: '1 / 2'"


def test_bool_assert():
    assert Fraction(1, 2)
    assert not Fraction(0)


def test_logic_operators():
    assert Fraction(2, 4) == Fraction(5, 10)
    assert not (Fraction(1, 2) != Fraction(1, 2))
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)
    assert Fraction(2, 4) == 0.5
    assert 0.5 == Fraction(2, 4)


def test_add():
    a = Fraction(2, 4)
    assert Fraction(2, 4) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) + 2 == Fraction(5, 2)
    assert Fraction(1, 2) + 2.5 == Fraction(3, 1)
    assert 2 + Fraction(1, 2) == Fraction(5, 2)

    # in place add
    b = a
    b += 2
    assert b is not a
    assert b == Fraction(5, 2)


def test_subtraction():
    a = Fraction(2, 4)
    assert Fraction(2, 4) - Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(5, 2) - 2 == Fraction(1, 2)
    assert 2 - Fraction(3, 2) == Fraction(1, 2)
    assert 3.5 - Fraction(3, 2) == Fraction(2, 1)

    # in place sub
    b = a
    b -= 2
    assert b is not a
    assert b == Fraction(-3, 2)


def multiplication():
    a = Fraction(2, 4)
    assert Fraction(1, 3) * 3 == 1
    assert Fraction(2, 3) * Fraction(12, 4) == 2
    assert 2 * Fraction(3, 2) == 3

    # in place mul
    b = a
    b *= 2
    assert b is not a
    assert b == 1


def test_division():
    a = Fraction(2, 4)
    assert Fraction(2, 3) / Fraction(2, 3) == 1
    assert Fraction(2, 3) / Fraction(4, 3) == Fraction(1, 2)
    assert 2 / Fraction(4, 3) == Fraction(3, 2)

    # in place div
    b = a
    b /= 2
    assert b is not a
    assert b == Fraction(1, 4)


def test_negative_int():
    assert -Fraction(1, 2) == Fraction(-1, 2)
    assert abs(Fraction(-1, 2)) == Fraction(1, 2)
