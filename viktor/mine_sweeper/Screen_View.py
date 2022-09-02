import Game_Session


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def update_screen(self, current_state):

        for row in current_state:
            for element in row:
                print(element, end='   ')
            print()
        # print(current_state)

