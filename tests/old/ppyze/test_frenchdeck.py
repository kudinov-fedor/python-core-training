import pytest

from homework.homework_9.frenchdeck import FrenchDeck, Card


def test_len():
    deck = FrenchDeck()
    assert len(deck) == 52


def test_get_item():
    deck = FrenchDeck()
    assert deck[0] == Card('2', 'spades')


def test_set_item():
    deck = FrenchDeck()
    deck[51] = Card('2', 'spades')
    assert len(deck) == 52
    assert deck[51] == Card('2', 'spades')
