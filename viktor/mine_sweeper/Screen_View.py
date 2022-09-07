import Game_Session


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def render_field(self, current_state):

        for row in current_state:
            for element in row:
                print(element, end='   ')
            print()
        # print(current_state)

    def update_screen(self, last_screen=False):
        state = [[None for j in range(self.session.width)] for i in range(self.session.height)]
        for i in range(self.session.height):
            for j in range(self.session.width):
                cell = (i, j)
                if cell in self.session.mines and last_screen:
                    value = "*"
                elif cell in self.session.guesses:
                    value = self.session.count_mines_around(cell)
                else:
                    value = "-"
                state[i][j] = value
        self.render_field(state)

