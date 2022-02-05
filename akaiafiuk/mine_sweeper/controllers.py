from random import randint


def next_move_automatic(field) -> tuple:
    """
    A function which generates next user's try
    :param field: Field object
    :return: tuple of coordinates
    """
    x = randint(0, field.width - 1)
    y = randint(0, field.height - 1)
    coord = x, y
    return coord


def next_move_user(field) -> tuple:
    """
    A function that generates next try using user input
    :param field: Field object
    :return: Tuple with coordinates entered by user
    """
    x, y = map(int, input('Input x, y and press Enter').split(','))
    x, y = x - 1, y - 1
    coord = x, y
    return coord
