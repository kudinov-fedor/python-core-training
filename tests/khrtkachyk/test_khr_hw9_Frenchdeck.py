import pytest
from khr_hw9_Frenchdeck import FrenchDeck, Card

deck = FrenchDeck()


def test_item_in_deck():
    assert Card(rank='A', suit='clubs') in deck
    assert Card(rank='B', suit='clubs') not in deck
    assert Card(rank='A', suit='empty') not in deck
    assert deck.ranks == ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    assert sorted(deck.suits) == ['clubs', 'diamonds', 'hearts', 'spades']


def test_len():
    assert len(deck) == 52
    assert len(deck) != 0
    for i in range(len(deck)):
        assert type(i) == int


@pytest.mark.parametrize("par, res", [
    (6, Card(rank='8', suit='spades')),
    (slice(0, 2, None), [Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]),
    (slice(51, None), [Card(rank='A', suit='hearts')]),
    (slice(0, None, 51), [Card(rank='2', suit='spades'), Card(rank='A', suit='hearts')])
])
def test_get_item(par, res):
    assert deck[par] == res


def test_getitem_by_param():
    assert deck[0].rank == "2"
    assert deck[51].suit == "hearts"


def test_iterable():
    dic = {}
    for n, card in enumerate(deck, 1):
        dic.update({n: card})
    assert dic.get(52) == Card(rank='A', suit='hearts')


def test_reverse_deck():
    lst = []
    for card in reversed(deck):
        lst.append(card)
    assert lst[0] == Card(rank='A', suit='hearts')


def test_set_item():
    deck[0] = deck[0]._replace(rank="new_rank")
    assert deck[0] == Card(rank='new_rank', suit='spades')


def test_update_item_by_param():
    card = None
    for card in deck:
        if card.rank == "A":
            card = card._replace(suit="new_suit")
    assert card == Card(rank='A', suit='new_suit')
