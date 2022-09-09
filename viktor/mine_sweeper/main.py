import game_session as game
from screen_view import ScreenView


def get_input(arg):
    return int(input(f'Provide please {arg}:'))


def get_parameters():
    height = get_input("height of field")
    width = get_input("width of field")
    mines_count = get_input("count of mines")
    return height, width, mines_count


if __name__ == "__main__":
    while True:
        try:
            game_session = game.GameSession(*get_parameters())
        except Exception as error:
            ScreenView.fire_alert(message=error)
        else:
            game_session.main()
            break


