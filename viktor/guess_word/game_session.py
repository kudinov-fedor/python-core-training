from screen_view import ScreenView
from message import Message

class GameSession:
    ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, task: str, desc: str):
        self.task = task
        self.desc = desc
        self.tries = []
        self.screen = ScreenView(self)

    def get_current_state(self):
        current_state = ""
        for x in self.task:
          current_state += x if x in self.tries else "*"
        return current_state

    def user_make_guess(self) -> str:
        """
        Receive input from user, normalize
        """
        return input('Input any letter: ').lower()
      
    def win(self) -> bool:
        """
        Check if all letters are guessed
        """
        return self.get_current_state() == self.task
      
    def guess_is_valid(self, guess: str) -> bool: # Here True or False
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
      self.screen.show_start_screen(self.desc, len(self.task))

      while not self.win():
        guess = self.user_make_guess()
        if not self.guess_is_valid(guess):
            self.screen.fire_alert(message=Message.INVALID.format(guess=guess))
            continue

        self.save_guess(guess) 
        current_message = Message.CORRECT if guess in self.task else Message.WRONG           
        self.screen.fire_alert(message=current_message)
        current_state = self.get_current_state()
        self.screen.show_current_state(current_state)

      self.screen.fire_alert(message=Message.WIN)