from mizo.task_frenchdeck import FrenchDeck, Card

deck = FrenchDeck()


def test_cards_in_french_deck():
    assert FrenchDeck.ranks == ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    assert FrenchDeck.suits == ['spades', 'diamonds', 'clubs', 'hearts']
    assert 'A' in deck.ranks
    assert 'eyes' not in deck.suits


def test_len_of_cards():
    assert len(deck) == 52
    assert len(deck) != 0


def test_card_position():
    assert deck[0] == Card('2', 'spades')
    assert deck[10] == Card('Q', 'spades')
    assert deck[-1] == Card('A', 'hearts')


def test_if_no_duplicates():
    assert len(deck) == len(set(deck))


def test_all_combinations_present():
    all_combinations = [(rank, suit) for suit in deck.suits for rank in deck.ranks]
    for combination in all_combinations:
        assert combination in deck
