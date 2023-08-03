import argparse
from random import randint


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
    WIN = "You win"
    CORRECT = "Correct"
    INPUT_REQUEST = "Make a guess"


# todo read random task from a file
def get_task(args) -> tuple:
    """
    Function which reads tasks from a file and gets random task
    """
    path = args.path
    sep = args.sep
    with open(path, "r") as f:
        lines = f.readlines()
        line = lines[randint(0, len(lines) - 1)]
        _task, _description = line.split(sep)
        return _task, _description


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self):
        """
        Print start screen
        """
        print(self.session.desc)

    def fire_alert(self, message: str):
        """
        Print message to console
        """
        print(message)

    def show_current_state(self):
        """
        Print current state of game
        """
        print("Current state:")
        print(f" - You made {len(self.session.tries)} tries")
        print(f" - Your tries: {', '.join(self.session.tries)}")


class GameSession:
    ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

    def user_make_guess(self) -> str:
        """
        Receive input from user, normalize
        """
        return input(f"{Message.INPUT_REQUEST}\n").lower()

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """
        return task in self.tries

    def guess_is_valid(self, guess: str) -> bool:
        """
        Check if input from user is valid
        """
        return all([char in self.ALLOWED_CHARS for char in guess])

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
