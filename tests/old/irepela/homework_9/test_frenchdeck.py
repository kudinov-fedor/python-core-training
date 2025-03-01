from irepela.homework_9.french_deck import FrenchDeck, Card


def test_french_deck():
    deck = FrenchDeck()

    assert len(deck) == 52
    assert deck[0] == Card(rank='2', suit='spades')
    assert deck[51] == Card(rank='A', suit='hearts')
    assert deck[:3] == [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    assert Card('5', 'clubs') in deck
    assert Card('blablabla', 'xyz') not in deck

    deck[0] = deck[-1]
    assert deck[0] == Card(rank='A', suit='hearts')
    assert [card for card in deck] == list(deck)
    first, *other = deck
    assert first == Card(rank='A', suit='hearts')
    assert len(other) == 51
