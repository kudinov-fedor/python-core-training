from random import randint
from typing import Union

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]
DEBUG = True


class Field:

    def __init__(self, height: int, width: int, mines_count: Union[int, list] = 0):
        """
        Initialize the field and assemble mines
        :param height: field height
        :param width: field width
        :param mines_count: int: count of mines inside the field | list: list of tuples with mine coordinates
        """
        self.field = [["."] * width for _ in range(height)]
        self.mines = self.create_mines(mines_count) if isinstance(mines_count, int) else mines_count

    @property
    def width(self):
        return len(self.field[0])

    @property
    def height(self):
        return len(self.field)

    def create_mines(self, count: int) -> list:
        """
        A function which returns a list of coordinates corresponding to mines
        :param count: Count of mines
        :return: list of mine coordinates
        """
        mines = list()
        counter = 0
        while counter < count:
            x = randint(1, self.width - 1)
            y = randint(1, self.height - 1)
            coord = x, y
            if coord in mines:
                continue
            mines.append(coord)
            counter += 1
        if DEBUG:
            print(mines)
        return mines

    def display_field(self) -> None:
        """
        Display the field
        :return: None
        """
        for i in self.field:
            print(i)
        print("-" * len(self.field[0]))

    def mines_count(self, guess_coordinates: tuple) -> int:
        """
        Returns an int with number of mines around the cell
        :param guess_coordinates: a tuple with x and y coordinates of a choice
        :return: int with number of mines around
        """
        return sum((guess_coordinates[0] + dx, guess_coordinates[1] + dy) in self.mines for dx, dy in DELTAS)

    def set_sign(self, guess_coordinates: tuple) -> None:
        """
        Sets sign on the field.  * if mine else: mines_around
        :param guess_coordinates: a tuple with x and y coordinates
        :return: None
        """
        sign = "*" if self.is_mine(guess_coordinates) else str(self.mines_count(guess_coordinates))
        self.field[guess_coordinates[1]][guess_coordinates[0]] = sign

    def is_coordinate_in_field(self, coord_to_verify: tuple) -> bool:
        """
        Verify if given coordinates are within the field boundaries
        :param coord_to_verify: a tuple with x and y coordinates
        :return: bool if a coordinate is within the field boundaries
        """
        x, y = coord_to_verify
        return x in range(self.width) and y in range(self.height)

    def is_mine(self, coord_to_verify: tuple) -> bool:
        """
        Returns True if coordinate in mines, else return False
        :param coord_to_verify: a coordinate to verify
        :return: bool if coord_to_verify in mines
        """
        return coord_to_verify in self.mines

    def empty_cells(self) -> list:
        """
        Returns a list of all available closed cells
        :return: list of tuples with all available closed cells
        """
        empty_cells = list()
        for y_index, y in enumerate(self.field):
            for x_index, x in enumerate(y):
                if x == '.':
                    empty_cells.append((x_index, y_index))
        if DEBUG:
            print(empty_cells)
        return empty_cells


def next_move(field) -> tuple:
    """
    A function which generates next user's try
    :return: tuple of coordinates
    """
    x = randint(0, field.width - 1)
    y = randint(0, field.height - 1)
    coord = x, y
    if DEBUG:
        print(coord)
    return coord


def auto_run_the_game(height: int = 10, width: int = 7, mines_number: int = 3):
    field = Field(height, width, mines_number)

    while True:

        x, y, = next_move(field)
        guess = x, y
        if DEBUG:
            print("Guess: " + str(guess))

        # set sign
        field.set_sign(guess)

        # display
        field.display_field()

        if field.is_mine(guess):
            break


def run(height: int = 5, width: int = 7, mines_number: int = 3) -> None:
    """
    Runs a mine sweeper game
    :param height: Game field height
    :param width: Game field width
    :param mines_number: Count of mines that the field will contain
    :return: None
    """
    field = Field(height, width, mines_number)

    while True:
        try:
            x, y = map(int, input('Input x, y and press Enter').split(','))
        except Exception:
            print("Enter 2 coordinates using comma as a separator.")
            continue
        x, y = x - 1, y - 1
        guess = x, y

        # set sign
        if guess in field.empty_cells():
            field.set_sign(guess)
        else:
            print("Coordinates already used or incorrect.")

        # display
        field.display_field()

        if field.is_mine(guess):
            break

        if not [value for value in field.empty_cells() if not field.is_mine(value)]:
            print("You've won. Congratulations!")
            break


if __name__ == "__main__":
    run()
