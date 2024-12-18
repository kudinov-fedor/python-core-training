import random
import csv
from enum import Enum
from pathlib import Path
import re


def get_data_from_file(csv_file, directory=None):
    """
    function for reading data from CSV file
    """
    base_dir = Path(__file__).resolve().parent.parent
    data_file = base_dir.joinpath(directory).joinpath(csv_file)

    with open(data_file) as file:
        reader = csv.reader(file)
        data = [','.join(row) for row in reader]

    return data


class Message(Enum):
    """
    Class for messages
    """

    INVALID = 'Invalid value. Try again.'
    WRONG = 'Wrong value. Try again!'
    WIN = 'You guess the word. Congratulation!'
    CORRECT = 'Correct! This letter is in the word.'
    INPUT_REQUEST = 'Enter the letter: '


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self):
        print(self.session.desc)
        print(["_" for _ in self.session.task])

    @staticmethod
    def fire_alert(message: str):
        print(message)

    def show_current_state(self):
        print(["_" if letter not in self.session.tries else letter for letter in self.session.task])


class GuessProcessing:
    ALLOWED_CHARS = r"[a-zA-Z]"

    def __init__(self, session: "GameSession"):
        self.session = session

    @staticmethod
    def user_make_guess() -> str:
        """
        Receive input from user, normalize
        """

        return input(Message.INPUT_REQUEST.value).strip().lower()

    def guess_is_valid(self, guess: str) -> bool:
        """
        Check if input from user is valid
        """

        return len(guess) == 1 and re.match(self.ALLOWED_CHARS, guess)


class GameSession:

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)
        self.guess = GuessProcessing(self)

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """

        return set(self.task).issubset(self.tries)

    def save_guess(self, guess: str):
        """
        Save guess in tries
        """

        self.tries.append(guess)

    def main(self):
        self.screen.show_start_screen()

        while not self.win():
            guess = self.guess.user_make_guess()
            if not self.guess.guess_is_valid(guess):
                self.screen.fire_alert(message=Message.INVALID.value)

                continue

            self.save_guess(guess)

            if guess in self.task:
                self.screen.fire_alert(message=Message.CORRECT.value)
            else:
                self.screen.fire_alert(message=Message.WRONG.value)

            self.screen.show_current_state()

        self.screen.fire_alert(message=Message.WIN.value)


if __name__ == "__main__":
    words = get_data_from_file(csv_file="words.csv", directory="homework_11")
    random_word = random.choice(words)
    GameSession(random_word, 'You need to guess all letters in the random word.').main()
    print(random_word)
