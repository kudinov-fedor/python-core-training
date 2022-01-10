from random import randint

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]
DEBUG = True


def create_mines(count: int, field: list) -> list:
    """
    A function which returns a list of coordinates corresponding to mines
    :param count: Count of mines
    :param field: Field representation as a list
    :return: list of mine coordinates
    """
    mines = list()
    counter = 0
    while counter < count:
        x = randint(1, len(field[0]) - 1)
        y = randint(1, len(field) - 1)
        coord = x, y
        if coord in mines:
            continue
        mines.append(coord)
        counter += 1
    if DEBUG:
        print(mines)
    return mines


def setup(height: int, width: int) -> list:
    """
    Create a field in form of list
    :param height: field height
    :param width: field width
    :return: field representation as a list
    """
    field = [["."] * width for _ in range(height)]
    return field


def display_field(field: list) -> None:
    """
    Display the field
    :param field: field representation as a list
    :return: None
    """
    for i in field:
        print(i)
    print("-" * len(field[0]))


def mines_count(guess_coordinates: tuple, mines: list) -> int:
    """
    Returns an int with number of mines around the cell
    :param guess_coordinates: a tuple with x and y coordinates of a choice
    :param mines: a list of tuples with mine coordinates
    :return: int with number of mines around
    """
    return sum((guess_coordinates[0] + dx, guess_coordinates[1] + dy) in mines for dx, dy in DELTAS)


def next_move(field: list) -> tuple:
    """
    A function which generates next user's try
    :return: tuple of coordinates
    """
    x = randint(0, len(field[0]) - 1)
    y = randint(0, len(field) - 1)
    coord = x, y
    if DEBUG:
        print(coord)
    return coord


def set_sign(guess: tuple, mines: tuple, field: list) -> None:
    """
    Sets sign on the field.  * if mine else: mines_around
    :param guess: a tuple with x and y coordinates
    :param mines: a list of tuples with mine coordinates
    :param field: field representation as a list
    :return: None
    """
    sign = "*" if guess in mines else str(mines_count(guess, mines))
    field[guess[1]][guess[0]] = sign


def run(height: int = 10, width: int = 7, mines_number: int = 3) -> None:
    """
    Runs a mine sweeper game
    :param height: Game field height
    :param width: Game field width
    :param mines_number: Count of mines that the field will contain
    :return: None
    """
    field = setup(height, width)
    mines = create_mines(mines_number, field)

    while True:

        x, y, = next_move(field)
        guess = x, y

        # set sign
        set_sign(guess, mines, field)

        # display
        display_field(field, width)


if __name__ == "__main__":
    run()
