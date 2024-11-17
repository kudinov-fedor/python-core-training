import random


class Message:
    INPUT_COLUMNS_REQUEST = "Please enter number of columns: "
    INPUT_ROWS_REQUEST = "Please enter number of rows: "
    INPUT_MINES_REQUEST = "Please enter number mines: "
    INPUT_MOVE_REQUEST = "Please put your move in format 'x y': "


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def update_screen(self, show_mines=False):
        table = [["___" for _ in range(self.session.width)]
                 for _ in range(self.session.height)]

        if show_mines:
            for x, y in self.session.mines:
                table[y][x] = " * "

        for x, y in self.session.guesses:
            table[y][x] = self.session.guesses[x, y]

        format_int = lambda i: format(str(i).zfill(2), "^4")

        print("      " + "".join(map(format_int, range(self.session.width))))
        for i, row in enumerate(table):
            print(format_int(i) + "  " + ".".join(map(lambda i: format(str(i), "^3"), row)))

    @staticmethod
    def show_alert(message: str):
        print(message)


class GameSession:

    NEIGHBOURS = [(0, 1), (0, -1),
                  (1, 1), (1, 0), (1, -1),
                  (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, height: int, width: int, mine_count: int):
        self.height = height
        self.width = width
        self.guesses = {}  # key coord, value - mines around
        self.mines = self.prepare_mines(mine_count)
        self.screen = ScreenView(self)

    def prepare_mines(self, mine_count: int) -> list:
        """
        Prepare list of mines coordinates based on config
        """
        cells = [(x, y) for x in list(range(self.width)) for y in list(range(self.height))]
        random.shuffle(cells)
        return cells[:mine_count]

    @staticmethod
    def normalize_user_input() -> tuple[int, ...]:
        """
        Receive coordinates as input from user
        """
        data = input(Message.INPUT_MOVE_REQUEST).strip()
        return tuple(map(int, data.split()))

    @staticmethod
    def validate_user_input(data: tuple[int, ...]):
        """
        Receive input from user, normalize, validate, convert to ints

        Raise errors if required
        - Raise ValueError
        - Raise OutOfBounds error
        """
        if len(data) != 2:
            raise ValueError
        less_than_zero = data[0] < 0 or data[1] < 0
        more_than_range = data[0] >= width or data[1] >= height
        if less_than_zero or more_than_range:
            raise IndexError

    def empty_cells(self) -> list:
        """
        Return cells, which are yet not opened and do not contain mines
        """
        return [(x, y)
                for x in list(range(self.width))
                for y in list(range(self.height))
                if (x, y) not in self.mines and (x, y) not in self.guesses]

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
        Save user input
        """
        queue = [coord]
        while queue:
            x, y = queue.pop()
            mines_around = self.mines_around((x, y))
            self.guesses[(x, y)] = mines_around

            # recursively open all neighbour cells if current cell == 0
            if mines_around == 0:
                neighborhood_cells = {(dx + x, dy + y) for dx, dy in self.NEIGHBOURS}
                cells_to_check = neighborhood_cells.intersection(self.empty_cells())
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
            data = self.normalize_user_input()

            # validate and normalize
            # if error - catch, inform user and return to start
            try:
                self.validate_user_input(data)
            except ValueError:
                self.screen.show_alert(f"There should be only two int numbers x y: {data}")
                continue
            except IndexError:
                self.screen.show_alert(f"Entered numbers: {data} are not in range: {width, height}")
                continue

            # if mine - end game
            if self.is_mine(data):
                self.screen.show_alert(f"There is a mine here, you have lost the game: {data}")
                break

            # save user input
            self.save_guess(data)

        # if win show win message
        else:
            self.screen.show_alert("You Won!!!")

        # show screen last time
        self.screen.update_screen(True)


if __name__ == "__main__":
    try:
        width = int(input(Message.INPUT_ROWS_REQUEST).strip())
        height = int(input(Message.INPUT_COLUMNS_REQUEST).strip())
        mine_count = int(input(Message.INPUT_MINES_REQUEST).strip())
        GameSession(height, width, mine_count).main()
    except ValueError:
        print("Please enter one int value for each input!")
