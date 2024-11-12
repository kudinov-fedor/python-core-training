import random
import argparse

import emoji

CONFIG = {
    'test': (3, 3, 1),
    'easy': (10, 10, 10),
    'medium': (20, 30, 25),
    'hard': (30, 40, 100)
}


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--difficulty',
                        action='store',
                        dest='difficulty',
                        default='easy',
                        help='easy | medium | hard')

    return parser.parse_args()


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def update_screen(self, show_mines: bool = False):
        table = [[emoji.emojize(':white_large_square:') for _ in range(self.session.width)]
                 for _ in range(self.session.height)]

        if show_mines:
            for x, y in self.session.mines:
                table[y][x] = emoji.emojize(':fire:')

        for x, y in self.session.guesses:
            table[y][x] = self.session.guesses[x, y]

        format_int = lambda i: format(str(i).zfill(2), "^4")

        print("      " + "".join(map(format_int, range(self.session.width))))
        for i, row in enumerate(table):
            print(format_int(i) + "  " + ".".join(map(lambda i: format(str(i), "^3"), row)))

    def show_alert(self, message: str):
        print(message)


class GameSession:
    NEIGHBOURS = [(0, 1), (0, -1),
                  (1, 1), (1, 0), (1, -1),
                  (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, height, width, mine_count):
        self.height = height
        self.width = width

        self.guesses = {}  # key coord, value - mines around
        self.mines = []  # list of coordinates

        self.mines = self.prepare_mines(mine_count)
        self.screen = ScreenView(self)

    def prepare_mines(self, mine_count: int) -> list:
        """
        Prepare list of mines coordinates based on config
        """
        cells = self.empty_cells()
        random.shuffle(cells)
        return cells[:mine_count]

    def receive_user_input(self) -> str:
        """
        Receive coordinates as input from user
        """
        return input("Make a move in format 'x y': ")

    def normalize_user_input(self, data: str) -> tuple:
        """
        Receive input from user, normalize, validate, convert to ints

        Raise errors if required
        - Raise ValueError
        - Raise OutOfBounds error
        """
        data = tuple(map(int, data.strip().split()))
        assert len(data) == 2
        assert data in self.empty_cells() + self.mines
        return data

    def empty_cells(self) -> list:
        return [(x, y)
                for x in list(range(self.width))
                for y in list(range(self.height))
                if (x, y) not in self.mines
                and (x, y) not in self.guesses]

    def in_field(self, coord: tuple) -> bool:
        """
        Check that coord is in field
        """
        return coord in self.empty_cells()

    def is_mine(self, coord: tuple) -> bool:
        """
        Check if there is a mine under coord
        """
        return coord in self.mines

    def mines_around(self, coord: tuple) -> int:
        """
        Calculate, how many mines are in neighbouring cells
        """
        x, y = coord
        return sum((x + dx, y + dy) in self.mines
                   for (dx, dy) in self.NEIGHBOURS)

    def save_guess(self, coord: tuple):
        """
        Save user input,
        in case if cell is 0, recursively open neighbour cells
        """
        queue = [coord]
        while queue:
            x, y = queue.pop()
            mines_around = self.mines_around((x, y))
            self.guesses[(x, y)] = mines_around

            # recursively open all neighbour cells if current cell == 0
            if mines_around == 0:
                neigbout_cells = {(dx + x, dy + y) for dx, dy in self.NEIGHBOURS}
                cells_to_check = neigbout_cells.intersection(self.empty_cells())
                queue.extend(cells_to_check)

    def win(self):
        """
        Check if user wins the game
        """
        return not self.empty_cells()

    def main(self):
        while not self.win():
            # show screen with current state
            self.screen.update_screen()
            # input from user
            data = self.receive_user_input()

            # validate and normalize
            # if error - catch, inform user and return to start
            try:
                data = self.normalize_user_input(data)
            except Exception:
                self.screen.show_alert("Wrong data: {}".format(data))
                continue

            # if mine - end game
            if self.is_mine(data):
                self.screen.show_alert("Is a mine, you loose: {}".format(data))
                break

            # save user input
            self.save_guess(data)

        # if win show win message
        else:
            self.screen.show_alert("You Win")

        # show screen last time
        self.screen.update_screen(show_mines=True)


if __name__ == "__main__":
    args = parse_args()
    height, width, mine_count = CONFIG.get(args.difficulty) or CONFIG["easy"]
    GameSession(height, width, mine_count).main()
