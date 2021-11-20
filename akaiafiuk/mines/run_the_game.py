from akaiafiuk.mines.mines_simplified import BattleField

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
    field = BattleField()
    field.assemble_mine()
    field.assemble_mine()
    field.assemble_mine()
    field.get_field()

    # Following line can be used for debug purposes to verify mines position
    # field.get_mines()

    while True:

        # End the game in case when all cells are open
        star_count = 0
        for row in field.field_to_print:
            star_count += row.count('*')
        if star_count == 2:
            print('$' * 30)
            print('$' * 30)
            print('$' * 30)
            print('$$ === WE HAVE A WINNER === $$')
            print('$' * 30)
            print('$' * 30)
            print('$' * 30)
            exit(0)

        # Get coordinates from user input and open the cell
        x = input("Input x coordinates and hit Enter: ")
        y = input("Input y coordinates and hit Enter: ")
        coordinates = (int(x) - 1, int(y) - 1)
        field.pick_cell(coordinates)


if __name__ == "__main__":
    TheGame()
