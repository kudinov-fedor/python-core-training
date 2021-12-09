from akaiafiuk.mines.mines_simplified import BattleField, BattlefieldView

DEBUG = True

rules_str = """
            The numbers on the board represent how many bombs are adjacent to a square.
            For example, if a square has a "3" on it, then there are 3 bombs next to that square.
            The bombs could be above, below, right left, or diagonal to the square. Avoid all the bombs
             and expose all the empty spaces to win Minesweeper.
            """


class TheGame:
    print('-*-' * 15)
    print('Hi and welcome to the mines console game')
    print("Rules: ", rules_str)
    print('Hit "Enter" to continue')
    print('-*-' * 15)
    input()
    x = int(input('Enter field width and press "Enter": '))
    y = int(input('Enter field height and press "Enter": '))
    mines_count = int(input('Enter number of mines: '))
    field = BattleField(x, y, mines_count)
    field_view = BattlefieldView(x, y)
    field_view.get_field()

    # Following line can be used for debug purposes to verify mines position
    if DEBUG:
        field.get_mines()

    while True:

        # End the game in case when all cells are open
        star_count = 0
        for row in field_view.field_to_print:
            star_count += row.count('*')
        if star_count == field.mines_count:
            print('$' * 30)
            print('$' * 30)
            print('$' * 30)
            print('$$ === WE HAVE A WINNER === $$')
            print('$' * 30)
            print('$' * 30)
            print('$' * 30)
            exit(0)

        # Get coordinates from user input and open the cell
        x = int(input("Input x coordinates and hit Enter: ") or 0)
        y = int(input("Input y coordinates and hit Enter: ") or 0)
        coordinates = (x - 1, y - 1)
        cell_value = field.pick_cell(coordinates)
        if cell_value == '@':
            print('@' * 30)
            print('@@@ Oh crap, you loose @@@')
            print('@' * 30)
            field_view.renew_field(coordinates, cell_value)
            exit(0)
        field_view.renew_field(coordinates, cell_value)


if __name__ == "__main__":
    TheGame()
