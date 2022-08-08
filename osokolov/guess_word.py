from string import ascii_lowercase


class GameModel:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.tries = []

    def check_win(self):
        return all([i in self.tries for i in self.word])


class GameView:

    def start_game_message(self, hint):
        print('Welcome!')
        print(f'Guess the word: f{hint}  ')
        print('If you want ot quit the game input word: quit')

    def warning_message(self):
        print('Input correct data')

    def show_game_result(self, word: str, letters: list):
        print(''.join([letter if letter in letters else "*" for letter in word]))

    def win_message(self):
        print('You guess!')


class GameController:
    def __init__(self, word, hint):
        self.word = word.lower()
        self.hint = hint
        self.view = GameView()
        self.model = GameModel(self.word, self.hint)

    def start(self):
        self.view.start_game_message(self.hint)
        while True:
            answer = self.get_user_answer()
            if answer == 'quit':
                break
            if self.validate_user_answer(answer):
                self.model.tries.append(answer)
            else:
                self.view.warning_message()
                continue
            self.view.show_game_result(self.word, self.model.tries)
            if self.model.check_win():
                break
        self.view.win_message()

    @classmethod
    def validate_user_answer(cls, answer):
        try:
            return len(answer) == 1 and answer in ascii_lowercase
        except TypeError:
            return False

    @classmethod
    def get_user_answer(cls):
        return input('Your try: ')


def guess(word: str, hint: str):
    GameController(word, hint).start()
