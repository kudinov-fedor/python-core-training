import argparse
import random


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
    # path = args.path
    # sep = args.sep
    with open("file.txt", encoding='utf-8') as f:
        lines = f.readlines()  # lines - array
        splited_lines = list(map(lambda pair: pair.split(':'), lines))  # [ [word, description], []]
        random_pair = random.choice(splited_lines)
        return random_pair[0], random_pair[1].strip()


class ScreenView:

    def __init__(self, session: "GameSession"):
        self.session = session


    def show_start_screen(self):
        print('Welcome to the my first guess-word game!')
        # print('Description:', description) # first way          several args for function print
        # print('Description: ' + description) # second way       concatenation
        # print('Description: {}'.format(description) # third way interpolation
        print(f"Description: {self.session.desc}")  # 4th way       f-strings
        print(f"Length of guess word is {len(self.session.task)} letters - {'*' * len(self.session.task)}")

    def fire_alert(self, message=" "):
        print(f'-----{message}-----')


    def show_current_state(self, ):
        current_state = ""
        for x in self.se
            ssion.task:  # a p p l e
            current_state += x if x in self.session.tries else "*"          ####???

        print(current_state)


class GameSession:
    ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

# не место в основном классе потому что данные для репрезентации
    # def get_current_state(self):
    #     current_state = ""
    #     for x in self.task:  # a p p l e
    #         current_state += x if x in self.tries else "*"
    #     return current_state

    def user_make_guess(self) -> str:
        """
        Receive input from user, normalize
        """
        return input('Input any letter: ').lower()

        # if not self.guess_is_valid(guess_value):
        #   print(Message.INVALID.format(guess = guess_value)) # "Value {guess} is not valid".format()
        # else:
        #   return guess_value

    def win(self) -> bool:
        """
        Check if all letters are guessed
        """
        current_state = ""
        for x in self.task:  # a p p l e
            current_state += x if x in self.tries else "*"

        return current_state == self.task   # ?????????????

    def guess_is_valid(self, guess: str) -> bool:  # Here True or False
        """
        Check if input from user is valid
        """
        check_result = list(map(lambda letter: letter in self.ALLOWED_CHARS, guess))
        return all(
            check_result)  # all -> [h, e, 1, l, o] bool(1) True bool(2)  -> True                                                      all([True, True, False, True, True]) -> False

    # guees in ALLOWEDCHARS -> True/False
    # map(lambda letter: letter in self.ALLOWED_CHARS, guess)

    def save_guess(self, guess: str):
        """
        Save guess in tries
        """
        self.tries.append(guess)

    #   class A:
    #     def __init__(self, a):
    #       self.age = a
    #       self.name = 2

    #     def b(self):
    #       self.b

    # def main
    #   human1 = Human(4)
    # object_a.a # 4
    # human2 = Human(7)
    # object_b.a # 7

    def main(self):
        self.screen.show_start_screen()  # call method show_start_screen of ScreenView object

        while not self.win():
            guess = self.user_make_guess()
            if not self.guess_is_valid(guess):
                self.screen.fire_alert(message=Message.INVALID.format(guess=guess))
                continue

            self.save_guess(guess)
            current_message = Message.CORRECT if guess in self.task else Message.WRONG
            self.screen.fire_alert(message=current_message)
            # current_state = self.get_current_state()
            self.screen.show_current_state()

        self.screen.fire_alert(message=Message.WIN)
        # print(f"{self.get_current_state()} - is the task guess word")


if __name__ == "__main__":
    args = parse_args()
    task, description = get_task(1)
    GameSession(task, description).main()
