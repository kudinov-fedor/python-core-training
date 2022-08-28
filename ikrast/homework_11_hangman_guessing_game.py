import random


# read file and parse into a list
def read_source():
    words = {}
    with open("C:\\Users\\ikrast\\OneDrive - SoftServe, Inc\\Desktop\\GameSource.txt") as file:
        for line in file:
            (key, value) = line.split(":")
            words[key] = value
    return words


# randomly select a word
def choose_word():
    words = read_source()
    randomized_word = random.choice(list(words.keys()))
    hint = words[randomized_word]
    print('Hint: ', hint)
    return randomized_word


# draw the graphic according to the progress
def draw_grapic(chances):
    if chances == 6:
        print('+-----+\n'
              '  |   |\n'
              '      |\n'
              '      |\n'
              '      |\n'
              '      |\n'
              '=========')
    elif chances == 5:
        print('+-----+\n'
              '  |   |\n'
              '  O   |\n'
              '      |\n'
              '      |\n'
              '      |\n'
              '=========')
    elif chances == 4:
        print('+-----+\n'
              '  |   |\n'
              '  O   |\n'
              '  |   |\n'
              '      |\n'
              '      |\n'
              '=========')
    elif chances == 3:
        print('+-----+\n'
              '  |   |\n'
              '  O   |\n'
              ' /|   |\n'
              '      |\n'
              '      |\n'
              '=========')
    elif chances == 2:
        print('+-----+\n'
              '  |   |\n'
              '  O   |\n'
              ' /|\  |\n'
              '      |\n'
              '      |\n'
              '=========')
    elif chances == 1:
        print('+-----+\n'
              '  |   |\n'
              '  O   |\n'
              ' /|\  |\n'
              ' /    |\n'
              '      |\n'
              '=========')
    elif chances == 0:
        print('Game Over')
        print('+-----+\n'
              '  |   |\n'
              '  O   |\n'
              ' /|\  |\n'
              ' / \  |\n'
              '      |\n'
              '=========')

    # Hangman art
    # print('+-----+\n'
    # '  |   |\n'
    # '  O   |\n'
    # ' /|\  |\n'
    # ' / \  |\n'
    # '      |\n'
    # '=========')


def game_setup():
    stats = {'chances': 7, 'guesses': 0}

    # initial graphic
    print("*_* Welcome to Simple Hangman Game *_*")
    print('+-----+\n'
          '      |\n'
          '      |\n'
          '      |\n'
          '      |\n'
          '      |\n'
          '=========')
    return stats


# main game loop
def game_start():
    # get random word
    guess_word = choose_word()
    check_word = guess_word
    # get word length and initiate needed lists and dictionaries for answers
    word_length = len(guess_word)
    list_size = 0
    answer = ""
    correct_guess = []
    incorrect_guess = []
    # initialize stats
    stats = game_setup()
    chances = stats.get('chances')
    guesses = stats.get('guesses')
    guess = True
    # 7 chances because the hangman art consists of 7 body part characters

    # create empty list with the length of the word
    while list_size < word_length:
        correct_guess.insert(list_size, "")
        list_size = list_size + 1

    # game loop start
    while chances > 0:

        user_guess = input('Guess a character: ')

        for character in user_guess:
            if character in guess_word:
                # get char index in word
                save_char = guess_word.index(character)
                # replace char at proper position in dict
                # split the list in 2 parts at current character, insert and combine
                correct_guess = correct_guess[:save_char] + [character] + correct_guess[save_char + 1:]
                # store remaining character to be guessed
                remaining_char = guess_word
                # replace the guessed char with a blank space
                remaining_char = remaining_char[:save_char] + " " + remaining_char[save_char + 1:]
                # update remainig chars to be guessed
                guess_word = remaining_char
                guess = True

            # check for duplicate correct guessed chars
            elif character in answer:
                guess = True
                print("You tried that already.")

            # reduce chances on wrong guess
            else:
                guesses += 1
                incorrect_guess.append(character)
                print('\'-\'')
                guess = False
                break

            # process correct chars in a string for answer check
            word = str(correct_guess)
            word2 = word.strip("[', ]")
            answer = word2.replace("', '", "")

        # print chosen chars
        print(f"Correct: {correct_guess}")
        print(f"Incorrect: {incorrect_guess}")

        # check if all chars are guessed
        if answer == check_word:
            print("")
            print(".:*~*:._.:*~*:")
            print("Correct.")
            print(".:*~*:._.:*~*:")
            print(f"Word : {answer}")
            break

        # check for wrong guess
        if not guess:
            chances -= 1
            print(f"Wrong. You have {chances} more chances left.")
            # draw graphic
            draw_grapic(chances)
            guess = True


# start
game_start()
