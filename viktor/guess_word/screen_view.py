class ScreenView:
    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self, description, number_letters):
      print('Welcome to the my first guess-word game!')
      print(f"Description: {description}")
      print(f"Length of guess word is {number_letters} letters - {'*' * number_letters}")

    def fire_alert(self, message=" "):
      print(message)

    def show_current_state(self, state):
      print(state)