from collections import namedtuple
from random import choice

# Card is a namedtuple that represents a playing card.
Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    FrenchDeck is a class that represents a deck of cards.
    """

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value


if __name__ == "__main__":
    deck = FrenchDeck()
    deck1 = choice(deck)
    print(len(deck))
    print(deck[::])
    print(deck1)
    print(Card('A', 'spades') in deck)
