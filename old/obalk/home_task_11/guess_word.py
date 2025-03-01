import argparse
import csv
import random
import string


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--path',
                        action='store',
                        dest='path',
                        help='path to a file with tasks')

    parser.add_argument('-s', '--sep',
                        action='store',
                        default="|",
                        dest='sep',
                        help='separator for file with tasks')

    return parser.parse_args()


class Message:
    INVALID = "Wrong value '{guess}', try again"
    WRONG = "Wrong, try again"
    FOUND = "Already guessed letter, try again"
    WIN = "You win"
    CORRECT = "Correct"
    INPUT_REQUEST = "Make a guess "


def get_task(args) -> tuple:
    """
    Function which reads tasks from a file and gets random task
    """
    path = args.path
    sep = args.sep

    with open(path, mode="r", newline="") as file:
        tasks = list(csv.reader(file, delimiter=sep))
    task, description = map(str.strip, random.choice(tasks))
    return task, description


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self):
        print(self.session.desc)
        print(["*" for _ in self.session.task])

    @staticmethod
    def fire_alert(message):
        print(message)

    def show_current_state(self):
        print(["*" if letter not in self.session.tries else letter for letter in self.session.task])


class GameSession:
    ALLOWED_CHARS = string.ascii_lowercase

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

    def user_make_guess(self) -> str:
        """
        Receive input from user, normalize
        """
        return input(Message.INPUT_REQUEST).strip().lower()

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """
        # return "*" not in self.task
        return set(self.task).issubset(self.tries)

    def guess_is_valid(self, guess: str) -> bool:
        """
        Check if input from user is valid
        """
        return len(guess) == 1 and guess in self.ALLOWED_CHARS

    def save_guess(self, guess: str):
        """
        Save guess in tries
        """
        self.tries.append(guess)

    def main(self):
        self.screen.show_start_screen()

        while not self.win():
            guess = self.user_make_guess()
            if not self.guess_is_valid(guess):
                self.screen.fire_alert(message=Message.INVALID.format(guess=guess))
                continue
            if guess in self.tries:
                self.screen.fire_alert(message=Message.FOUND)
                continue
            self.save_guess(guess)

            if guess in self.task:
                self.screen.fire_alert(message=Message.CORRECT)
            else:
                self.screen.fire_alert(message=Message.WRONG)

            self.screen.show_current_state()

        self.screen.fire_alert(message=Message.WIN)


if __name__ == "__main__":
    args = parse_args()
    task, description = get_task(args)
    GameSession(task, description).main()
