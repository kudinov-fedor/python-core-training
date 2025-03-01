from homework.homework_9.frenchdeck import FrenchDeck, Card


def test_len():
    deck = FrenchDeck()
    assert len(deck) == 52


def test_get_first_item():
    deck = FrenchDeck()
    assert deck[0] == Card('2', 'spades')


def test_set_item():
    deck = FrenchDeck()
    assert deck[0] == Card('2', 'spades')
    deck[0] = Card('A', 'clubs')
    assert len(deck) == 52
    assert deck[0] == Card('A', 'clubs')


def test_suites_count():
    deck = FrenchDeck()
    assert len(deck.suits) == 4


def test_ranks_count():
    deck = FrenchDeck()
    assert len(deck.ranks) == 13
