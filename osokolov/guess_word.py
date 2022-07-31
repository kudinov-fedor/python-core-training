from string import ascii_lowercase

#
# class GameModel:
#     def __init__(self, word, hint):
#         self.word = word
#         self.hint = hint
#         self.tries = []
#
#     def save_latter(self, letter):
#         self.tries.append(letter)
#
#     def check_win(self) -> bool:
#         pass
#
#
# class GameView():
#     def start_game(self, data: GameModel):
#         print('Welcome!')
#         print(f'Guessing word is the {data.word}. It has {len(data.hint)} letters')
#         print('If you want ot quit the game input word: quit')
#
#     def get_guessing_word(self, word: GameModel):
#         guessing_word = ['_ '] * len(word)
#         print(guessing_word)
#
#     def end_game(self):
#         print('You guess the word !')
#         print('Goodbye !')
#
#
# class GameController:
#
#     def recive_letter(self):
#         #input
#
#         pass


def get_user_answer():
    return input('Your try: ')


def validate_user_answer(user_answer):
    try:
        return len(user_answer) == 1 and user_answer in ascii_lowercase
    except TypeError:
        return False


def show_game_result(word: str, letters: list):
    print(''.join([letter if letter in letters else "*" for letter in word]))


def check_win(word: str, letters: list):
    return all([i in letters for i in word])


def guess(word: str, hint: str):
    word = word.lower()
    tries = []
    print('Welcome!')
    print(f'Guess the word: f{hint}  ')
    print('If you want ot quit the game input word: quit')
    while True:
        # user answer
        answer = get_user_answer()
        # validation
        if answer == 'quit':
            break
        if validate_user_answer(answer):
            tries.append(answer)  # save user data
        else:
            print('Input correct data')
            continue
        # show current state
        show_game_result(word, tries)
        # check win
        if check_win(word, tries):
            break

    print('You guess!')
