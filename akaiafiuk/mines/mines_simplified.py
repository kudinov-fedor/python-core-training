from random import randrange
from itertools import product


class BattleField:

    # Create a battlefield with field to print to a user and field to assemble mines
    def __init__(self):
        self.field_to_print = [['*'] * 5 for _ in range(5)]
        self.field_mines = [[False] * 5 for _ in range(5)]

    # Draw current state of the battlefield
    def get_field(self):
        print('-----1----2----3----4----5--')

        for i in range(len(self.field_to_print)):
            print('-' + str(i + 1) + '-' + str(self.field_to_print[i]))

    # Draw mines. Debug purposes.
    def get_mines(self):
        for i in range(len(self.field_mines)):
            print(self.field_mines[i])

    # Put a mine on the field
    def assemble_mine(self):
        self.field_mines[randrange(5)][randrange(5)] = True

    # Open the cell on the battlefield
    def pick_cell(self, coordinates):
        x_coord, y_coord = coordinates
        if self.field_mines[y_coord][x_coord]:
            print('@@@ -- YOU LOOSE! -- @@@')
            self.field_to_print[y_coord][x_coord] = '@'
            self.get_field()
            exit(0)

        else:
            print('XX -- I"m alive! Continue -- XX')

            # Verify how many mines borders with the opened cell
            mines_count = 0
            x_inspect_cells = [0, +1, -1]
            y_inspect_cells = [0, +1, -1]
            if coordinates[1] == 0:
                x_inspect_cells.pop(-1)
            if coordinates[1] == 4:
                x_inspect_cells.pop(+1)
            if coordinates[0] == 0:
                y_inspect_cells.pop(-1)
            if coordinates[0] == 4:
                y_inspect_cells.pop(+1)

            for x, y in product(x_inspect_cells, y_inspect_cells):
                try:
                    if self.field_mines[coordinates[1] + x][coordinates[0] + y]:
                        mines_count += 1
                except IndexError:
                    continue

            # Open the cell and draw the current battlefield state
            if mines_count == 0:
                self.field_to_print[coordinates[1]][coordinates[0]] = '-'
            else:
                self.field_to_print[coordinates[1]][coordinates[0]] = str(mines_count)
            self.get_field()
