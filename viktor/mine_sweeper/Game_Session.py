import random
import Screen_View


class GameSession:
    def __init__(self, height: int, width, mine_count):
        if height * width < mine_count:
            raise Exception("Too small field")

        self.height = height
        self.width = width
        self.mines = self.prepare_mines(mine_count)

        # todo save guesses here,
        #  use list or dict, or 2d array, what ever comfortable
        self.guesses = []
        self.screen = Screen_View.ScreenView(self)

    def prepare_mines(self, mine_count: int) -> list:
        """
        Prepare list of mines coords based on config
        """
        coordinates = []
        # print("Empty:", coordinates)

        while len(coordinates) < mine_count:
            coord_x = random.randint(0, self.width-1)
            coord_y = random.randint(0, self.height-1)

            if (coord_x, coord_y) not in coordinates:
                coordinates.append((coord_x, coord_y))


        #     print("Current0", coordinates)
        # print("Final", coordinates)
        return coordinates

    def receive_user_input(self) -> str:
        """
        Receive coords as input from user
        """
        return input('Put two coorddinates splitted by space: ')

    def normalize_user_input(self, data: str) -> tuple:
        """
        Receive input from user, normalize, validate, convert to ints

        Raise errors if required
        - Raise ValueError
        - Raise OutOfBounds error
        """
        x, y = list(map(lambda coordinate: int(coordinate), data.strip().split(" ")))
        if not self.in_field((x, y)):
            raise Exception('OutOfBounds')

        return x, y

        # x, y = data.split(" ")
        # x = int(x)
        # y = int(y)

    def not_open_cells(self) -> list:
        """
        Retun cells, which are yet not opened and do not contain mines
        """
        not_open_cells_list = [(i, j)
                            for i in range(self.height)
                            for j in range(self.width)
                            if (i, j) not in (self.guesses + self.mines)]
        return not_open_cells_list


    def in_field(self, coord: tuple) -> bool:
        """
        Check that coord is in field
        """
        return coord[0] in range(self.width) and coord[1] in range(self.height)



    def is_mine(self, coord: tuple) -> bool:
        """
        Check if there is a mine under coord
        """
        return coord in self.mines

    def count_mines_around(self, coord: tuple) -> int:
        """
        Calculate, how many mines are in neighbouring cells
        """
        i, j = coord
        neighbouring_cells = [
            (i-1, j-1), (i, j-1), (i+1, j-1),
            (i-1, j), (i+1,j),
            (i-1, j+1), (i, j+1), (i+1, j+1)
        ]
        return len(list(filter(self.is_mine, neighbouring_cells)))


    def save_guess(self, coord: tuple):
        """
        Save user input
        """
        self.guesses.append(coord)

    def win(self):
        """
        Check if user wins the game
        """
        # if len(self.not_open_cells()) == 0:
        return not len(self.not_open_cells())  # return True if all cells except mines are opened

    def main(self):
        while not self.win():
            # show screen with current state

            self.screen.update_screen()

            # input from user
            user_input = self.receive_user_input()
            # validate and normalize, if error - catch, inform user and return to start
            try:
                coordinates = self.normalize_user_input(user_input)
            except ValueError:
                print('Not a number')

            except Exception as error:
                print('Out of  bounds error')
            else:
                if self.is_mine(coordinates):                    # if mine - end game
                    print('Here\'s mine - game over')
                    break
                self.save_guess(coordinates)                     # save user input

            # ...

        # show screen last time

        self.screen.update_screen(last_screen=True)

