import argparse
import random
import csv


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
    WIN = "You won"
    CORRECT = "Correct"
    INPUT_REQUEST = "Make a guess (one letter): "


def get_task(args) -> tuple:
    """
    Function which reads tasks from a file and gets random task
    """
    path = args.path
    sep = args.sep

    with open(path) as csvfile:
        file_tasks = list(csv.reader(csvfile, delimiter=sep))
    file_task, file_desc = random.choice(file_tasks)

    return file_task, file_desc


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self):
        print(f"Word description: {self.session.desc}")
        mask = ["*" for _ in self.session.task]
        print("   ".join(mask))

    @staticmethod
    def fire_alert(message: str):
        print(message)

    def show_current_state(self):
        mask = list("*" * (len(self.session.task) - len(self.session.tries)))
        print("   ".join(self.session.tries + mask))


class GameSession:

    ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

    @staticmethod
    def user_make_guess() -> str:
        """
        Receive input from user, normalize
        """
        return input(Message.INPUT_REQUEST).strip().lower()

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """
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

            if guess == self.task[len(self.tries)]:
                self.save_guess(guess)
                self.screen.fire_alert(message=Message.CORRECT)
            else:
                self.screen.fire_alert(message=Message.WRONG)

            self.screen.show_current_state()

        self.screen.fire_alert(message=Message.WIN)


if __name__ == "__main__":
    args = parse_args()
    task, description = get_task(args)
    GameSession(task, description).main()
