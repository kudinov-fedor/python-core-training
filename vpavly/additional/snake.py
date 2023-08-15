import curses
from curses import textpad
from random import randint


def print_score(stdscr, score):
    score_text = f"Score: {score}"
    shell_height, shell_width = stdscr.getmaxyx()
    stdscr.addstr(0, shell_width // 2 - len(score_text) // 2, score_text)
    stdscr.refresh()


def create_food(snake, area):
    food = None
    while food is None:
        food = [randint(area[0][0] + 1, area[1][0] - 1),
                randint(area[0][1] + 1, area[1][1] - 1)]
        if food in snake:
            food = create_food(snake, area)
    return food


def main(stdscr):
    curses.curs_set(0)  # Set cursor invisible
    stdscr.nodelay(1)  # No blocking screen
    stdscr.timeout(150)  # Wait user to press smth

    shell_height, shell_width = stdscr.getmaxyx()
    # Coordinates of game box [[Upper left corner], [Lower right corner]]
    game_area = [[3, 3], [shell_height - 3, shell_width - 3]]

    curses.textpad.rectangle(stdscr, game_area[0][0], game_area[0][1], game_area[1][0], game_area[1][1])
    stdscr.refresh()  # Update screen
    stdscr.getch()  # Wait user to press any key

    # Initial of snake
    snake = [[shell_height // 2, shell_width // 2 + 1],
             [shell_height // 2, shell_width // 2],
             [shell_height // 2, shell_width // 2 - 1]]  # Start snake in center with length of 3
    direction = curses.KEY_RIGHT
    for y, x in snake:
        stdscr.addstr(y, x, "*")

    # Initial of score
    score = 0
    print_score(stdscr, score)

    # Initial food
    food = create_food(snake, game_area)
    stdscr.addstr(food[0], food[1], "\U0001F354")

    while True:
        key = stdscr.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        head = snake[0]

        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]

        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], "*")

        if snake[0] == food:
            food = create_food(snake, game_area)
            stdscr.addstr(food[0], food[1], "\U0001F354")
            score += 1
            print_score(stdscr, score)
        else:
            stdscr.addstr(snake[-1][0], snake[-1][-1], ' ')
            snake.pop()

        if (snake[0][0] in [game_area[0][0], game_area[1][0]] or
                snake[0][1] in [game_area[0][1], game_area[1][1]] or
                snake[0] in snake[1:]):
            game_over_message = "Game Over! \N{unamused face}"
            stdscr.addstr(shell_height // 2, (shell_width // 2 - len(game_over_message) // 2), game_over_message)
            stdscr.nodelay(0)
            stdscr.getch()
            break
    stdscr.refresh()


curses.wrapper(main)
