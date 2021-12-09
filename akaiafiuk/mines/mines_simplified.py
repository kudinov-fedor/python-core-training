from random import randrange
from itertools import product


class BattleField:

    # Create a battlefield and assemble mines
    def __init__(self, width, height, mines_count=3):
        self.width = width
        self.height = height
        self.mines_count = mines_count
        self.field_mines = [[False] * width for _ in range(height)]
        for _ in range(mines_count):
            self.assemble_mine()

    # Draw mines. Debug purposes.
    def get_mines(self):
        for i in range(len(self.field_mines)):
            print(self.field_mines[i])

    # Put a mine on the field
    def assemble_mine(self):
        self.field_mines[randrange(self.width)][randrange(self.height)] = True

    # Open the cell on the battlefield
    def pick_cell(self, coordinates):
        x_coord, y_coord = coordinates
        if x_coord not in range(self.width) or y_coord not in range(self.height):
            return -1

        if self.field_mines[y_coord][x_coord]:
            cell_value = '@'

        else:
            # Verify how many mines borders with the opened cell
            mines_count = 0
            x_inspect_cells, y_inspect_cells = self.get_cells_to_inspect(coordinates)
            for x, y in product(x_inspect_cells, y_inspect_cells):
                try:
                    if self.field_mines[y_coord + y][x_coord + x]:
                        mines_count += 1
                except IndexError:
                    continue
                cell_value = mines_count

        return cell_value

    def get_cells_to_inspect(self, coordinates) -> tuple:
        """Returns a tuple with list of x and list of y coordinates to inspect"""
        x_coord, y_coord = coordinates
        x_inspect_cells = [0, +1, -1]
        y_inspect_cells = [0, +1, -1]

        if y_coord == 0:
            y_inspect_cells.pop(-1)
        if y_coord == self.height - 1:
            y_inspect_cells.pop(+1)

        if x_coord == 0:
            x_inspect_cells.pop(-1)
        if x_coord == self.width - 1:
            x_inspect_cells.pop(+1)

        return x_inspect_cells, y_inspect_cells


class BattlefieldView:

    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.field_to_print = [['*'] * width for _ in range(height)]

    def get_field(self):
        self.draw_top_line()
        for i in range(len(self.field_to_print)):
            print('-' + str(i + 1) + '-' + str(self.field_to_print[i]))

    # Draw the field again after shot
    def renew_field(self, coordinates, cell_value):
        x_coord, y_coord = coordinates
        if cell_value == -1:
            print("Index outside boundaries. Please repeat.")
        elif cell_value == 0:
            self.field_to_print[y_coord][x_coord] = '-'
        else:
            self.field_to_print[y_coord][x_coord] = str(cell_value)
        self.get_field()

    # Draw the top line to be able to see x coordinates
    def draw_top_line(self):
        print('-', end='')
        for item in [i + 1 for i in range(self.width)]:
            print(f'----{item}', end='')
        print('-')
