
class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def update_screen(self):
        ...


class GameSession:

    def __init__(self, height, width, mine_count):
        self.height = height
        self.width = width
        self.mines = self.prepare_mines(mine_count)

        # todo save guesses here,
        #  use list or dict, or 2d array, what ever comfortable
        self.guesses = None

        self.screen = ScreenView(self)

    def prepare_mines(self, mine_count: int) -> list:
        """
        Prepare list of mines coords based on config
        """

    def receive_user_input(self) -> str:
        """
        Receive coords as input from user
        """
        ...

    def normalize_user_input(self, data: str) -> tuple:
        """
        Receive input from user, normalize, validate, convert to ints

        Raise errors if required
        - Raise ValueError
        - Raise OutOfBounds error
        """
        ...

    def empty_cells(self) -> list:
        """
        Retun cells, which are yet not opened and do not contain mines
        """
        ...

    def in_field(self, coord: tuple) -> bool:
        """
        Check that coord is in field
        """

    def is_mine(self, coord: tuple) -> bool:
        """
        Check if there is a mine under coord
        """

    def mines_around(self, coord: tuple) -> int:
        """
        Calculate, how many mines are in neighbouring cells
        """

    def save_guess(self, coord: tuple):
        """
        Save user input
        """

    def win(self):
        """
        Check if user wins the game
        """

    def main(self):
        while not self.win():
            # show screen with current state
            # input from user
            # validate and normalize, if error - catch, inform user and return to start
            # if mine - end game
            # save user input
            ...

        # show screen last time


# todo entry point
#  get height, width, mines_count from input
#  use convenient data structure to store data
