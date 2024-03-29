import pytest

from hw9_frenchdeck import FrenchDeck, Card


@pytest.fixture()
def deck():
    return FrenchDeck()


def test_check_len(deck):
    assert len(deck) == 52


def test_check_position_1(deck):
    assert deck[1] == Card(rank='3', suit='spades')


def test_check_position_2(deck):
    assert deck[12] == Card(rank='A', suit='spades')


def test_check_slicing(deck):
    assert deck[20:22] == [Card(rank='9', suit='diamonds'), Card(rank='10', suit='diamonds')]


def test_check_slicing_2(deck):
    assert deck[11::13] == [Card(rank='K', suit='spades'), Card(rank='K', suit='diamonds'),
                            Card(rank='K', suit='clubs'), Card(rank='K', suit='hearts')]


def test_modify_deck(deck):
    deck[13:13] = [Card(rank='Joker', suit='red')]
    assert deck[13] == Card(rank='Joker', suit='red')


def test_modify_deck_1(deck):
    deck[52:52] = [Card(rank='Joker', suit='dark')]
    assert deck[-1] == Card(rank='Joker', suit='dark')
