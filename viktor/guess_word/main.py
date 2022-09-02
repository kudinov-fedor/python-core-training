from game_session import GameSession
import random

def get_task() -> tuple:
  """
  Function which reads tasks from a file and gets random task
  """
  with open("file.txt", encoding = 'utf-8') as f:
    lines = f.readlines()
    splited_lines = list(map(lambda pair: pair.split(':'), lines))
    random_pair = random.choice(splited_lines)
    return random_pair[0], random_pair[1].strip()

if __name__ == "__main__":
    task, description = get_task()
    GameSession(task, description).main()