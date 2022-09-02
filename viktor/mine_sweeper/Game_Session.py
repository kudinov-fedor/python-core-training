import random
import Screen_View


class GameSession:
    def __init__(self, height, width, mine_count):
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

        while True:
            coord_x = random.randint(0, self.width-1)
            coord_y = random.randint(0, self.height-1)

            condition = (coord_x, coord_y) in coordinates
            if condition:
                continue
            else:
                coordinates.append((coord_x, coord_y))
            if len(coordinates) == mine_count:
                break

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
        x, y = list(map(lambda coordinate: int(coordinate), data.split(" ")))
        if not self.in_field((x, y)):
            raise Exception('OutOfBounds')

        return x, y

        # x, y = data.split(" ")
        # x = int(x)
        # y = int(y)

    def empty_cells(self) -> list:
        """
        Retun cells, which are yet not opened and do not contain mines
        """
        #?????????????????????????????????????????????????????????????????????????????????????????
        empty_cells_list = []
        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)
                condition = cell not in (self.guesses + self.mines)
                if condition:
                    empty_cells_list.append(cell)
        return empty_cells_list


    def in_field(self, coord: tuple) -> bool:
        """
        Check that coord is in field
        """
        return 0 <= coord[0] < self.width and 0 <= coord[1] < self.height


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
        return sorted(self.guesses) == sorted(self.empty_cells())

    def get_current_state(self, last_screen=False):
        state = [[None for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)
                if cell in self.mines and last_screen:
                    value = "*"
                elif cell in self.guesses:
                    value = self.count_mines_around(cell)
                else:
                    value = "-"
                state[i][j] = value


                # state[i][j] = "-" if cell not in self.guesses else self.count_mines_around(cell)
        return state

    def main(self):
        while not self.win():
            # show screen with current state
            current_state = self.get_current_state()
            self.screen.update_screen(current_state)

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
        current_state = self.get_current_state(last_screen=True)
        self.screen.update_screen(current_state)

