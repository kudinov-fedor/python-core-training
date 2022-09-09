import random


class Message:
    INVALID = "Wrong value '{guess}', try again"
    WRONG = "Wrong, try again"
    WIN = "You win"
    CORRECT = "Correct"
    INPUT_REQUEST = "Make a guess"


# todo read random task from a file
def get_task() -> tuple:
    """
    Function which reads tasks from a file and gets random task
    """
    with open("file.txt", encoding='utf-8') as f:
        lines = f.readlines()
        splitted_lines = list(map(lambda pair: pair.split(':'), lines))
        random_pair = random.choice(splitted_lines)
        return random_pair[0], random_pair[1].strip()


class ScreenView:
    def __init__(self, session: "GameSession"):
        self.session = session

    def show_start_screen(self):
        print('Welcome to the my first guess-word game!')
        print(f"Description: {self.session.desc}")
        print(f"Length of guess word is {len(self.session.task)} letters - {'*' * len(self.session.task)}")

    @staticmethod
    def fire_alert(message=" "):
        print(f'-----{message}-----')

    def show_current_state(self, ):
        current_state = ""
        for x in self.session.task:
            current_state += x if x in self.session.tries else "*"

        print(current_state)


class GameSession:
    ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, task_: str, desc: str):
        self.task = task_
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

    @staticmethod
    def user_make_guess() -> str:
        """
        Receive input from user, normalize
        """
        return input('Input any letter: ').lower()

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """
        current_state = ""
        for x in self.task:  # a p p l e
            current_state += x if x in self.tries else "*"

        return "*" not in current_state

    def guess_is_valid(self, guess: str) -> bool:
        """
        Check if input from user is valid
        """
        check_result = list(map(lambda letter: letter in self.ALLOWED_CHARS, guess))
        return all(check_result)

    def save_guess(self, guess: str):
        """
        Save guess in tries
        """
        self.tries.append(guess)

    def main(self):
        self.screen.show_start_screen()                 # call method show_start_screen of ScreenView object

        while not self.win():
            guess = self.user_make_guess()
            if not self.guess_is_valid(guess):
                self.screen.fire_alert(message=Message.INVALID.format(guess=guess))
                continue

            self.save_guess(guess)
            current_message = Message.CORRECT if guess in self.task else Message.WRONG
            self.screen.fire_alert(message=current_message)
            self.screen.show_current_state()

        self.screen.fire_alert(message=Message.WIN)


if __name__ == "__main__":
    task, description = get_task()
    GameSession(task_=task, desc=description).main()

