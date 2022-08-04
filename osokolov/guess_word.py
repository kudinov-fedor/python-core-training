from string import ascii_lowercase


class GameModel:

    def check_win(self, word: str, letters: list):
        return all([i in letters for i in word])


class GameView:

    def get_user_answer(self):
        return input('Your try: ')

    def show_game_result(self, word: str, letters: list):
        print(''.join([letter if letter in letters else "*" for letter in word]))


class GameController:
    def __init__(self):
        self.view = GameView()
        self.model = GameModel()
        self.answer = self.view.get_user_answer()

    def validate_user_answer(self, answer):
        try:
            return len(answer) == 1 and answer in ascii_lowercase
        except TypeError:
            return False


def guess(word: str, hint: str):
    word = word.lower()
    tries = []
    print('Welcome!')
    print(f'Guess the word: f{hint}  ')
    print('If you want ot quit the game input word: quit')
    while True:
        controller = GameController()
        # user answer
        answer = controller.answer
        # validation
        if answer == 'quit':
            break
        if controller.validate_user_answer(answer):
            tries.append(answer)  # save user data
        else:
            print('Input correct data')
            continue
        # show current state
        controller.view.show_game_result(word, tries)
        # check win
        if controller.model.check_win(word, tries):
            break

    print('You guess!')

