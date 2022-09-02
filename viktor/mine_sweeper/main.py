import Game_Session as game


# import pdb; pdb.set_trace() # debugging

def get_input(arg):
    return int(input(f'Provide please {arg}:'))


def get_parameters():
    height = get_input("height of field")
    width = get_input("width of field")
    mines_count = get_input("count of mines")
    return (height, width, mines_count)


if __name__ == "__main__":

    # todo entry point
    #  get height, width, mines_count from input

    # height = get_input("height of field")
    # width = get_input("width of field")
    # mines_count = get_input("count of mines")
    while True:
        try:
            game_session = game.GameSession(*get_parameters())
            '''
            how this asteriks works (destructurization, unpacking)
            *[1, 2, 3] will be interpreted as 1, 2, 3
            example:
            array = [1, 2, 3]
             def get_three_numbers(num1, num2, num3):
               print(num1, num2, num3)
             we can call get_three_numbers like this:
             get_three_numbers(array[0], array[1], array[2])
             but obviously this way is better(readability)
            get_three_numbers(*array)
            '''
        except Exception as error:
            print(error)
            # import pdb; pdb.set_trace()
            # continue
        else:
            game_session.main()
            break

#  use convenient data structure to store data
