from homework.homework_9.frenchdeck import FrenchDeck, Card


def test_frenchdeck():
    game = FrenchDeck()
    # get length
    assert len(game.ranks) == 13
    assert len(game.suits) == 4
    assert len(game._cards) == 52

    # slicing
    assert game[1:5] == [Card(rank='3', suit='spades'),
                         Card(rank='4', suit='spades'),
                         Card(rank='5', suit='spades'),
                         Card(rank='6', suit='spades')]

    # sorting
    assert sorted(game.ranks) == ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q']
    assert sorted(game.ranks, reverse=True) == ['Q', 'K', 'J', 'A', '9', '8', '7', '6', '5', '4', '3', '2', '10']

    # boolean
    assert (Card(rank='3', suit='spades') in game) is True
    assert (Card(rank='Q', suit='triangle') in game) is False
    assert all(game) is True

    # get max min values
    assert max(game) == Card(rank='Q', suit='spades')
    assert min(game) == Card(rank='10', suit='clubs')

    # set item
    game[0] = Card(rank='0', suit='star')
    assert game[0] == Card(rank='0', suit='star')

    game._cards.append(Card(rank='100', suit='super'))
    assert Card(rank='100', suit='super') in game

    # remove item
    game._cards.pop()
    assert Card(rank='100', suit='super') not in game

    # iteration
    test_iter = iter(game)
    assert next(test_iter) == Card(rank='0', suit='star')
