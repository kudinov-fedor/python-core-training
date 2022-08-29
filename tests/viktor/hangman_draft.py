
def hangman(guess_word, prompt = "Guess word is related to feeling"):    #второй аргумент - подсказка
    print('Welcome to my first game "Guess the word"')
    print(prompt)
    guess_word = list(guess_word)
    guess_letters = ['*'] * len(guess_word)
    every_try = []
    available_letters = 'zxcvbnmasdfghjklqwertyuiop'

    while guess_letters != guess_word:
        x = input('Enter your letter: ').lower()
        every_try.append(x)
        if not x.isalpha():
            print('Please enter only letter')
            continue
        if x in guess_word:
            ind_arr = []
            for ind, el in enumerate(guess_word):
                if x == el:
                    guess_letters[ind] = x
            print('You did it')
            print(guess_letters)
        else:
            print('Try one more time')
            print(guess_letters)

    print('YOU WON')
    print(f'ALL LETTERS: {every_try}\nAmount: {len(every_try)}')


hangman('love')


#********************************



# print('Welcome to my first game "Guess the word"')
#
#
# guess_word = ['p', 'y', 't', 'h', 'o', 'y']                 # list with secret word
# guess_letters = ['*', '*', '*', '*', '*', '*']              # list with right guess letters
# wrong_letters = []                                          # list with wrong guess letters
#
# while guess_letters != guess_word:                          # loop with comparing two lists until two lists will be equal each other
#     x = input('Enter your letter: ')                        # input of guess letter
#     if x in guess_word:                                     # checking if guess letter exist in guess word
#         ind_arr = []                                        # temporary list to get appropriate index of guess letter
#         for ind, el in enumerate(guess_word):               # loop to find all indexes for all letters in guess word
#             if x == el:                                     # if input letter equal to any element in guess_word
#                 ind_arr.append(ind)                         # then put this index into temporary list ind_arr
#         for ind in ind_arr:                                 # check index in temporary list
#             guess_letters[ind] = x                          # put the inputted letter into the gues_letters by the right index
#         print('You did it')
#         print(guess_letters)
#         continue                                            # ???
#     print('Try one more time')
#     wrong_letters.append(x)                                 # storing all wrong letters
# print('YOU WON')
# print(f'WRONG LETTERS: {wrong_letters}\nAmount: {len(wrong_letters)}')



# print('Welcome to my first game "Guess the word"')
#
# print("Enter your first guess letter:")
#
# guess_word = 'python'
#
# guess_letters = '******p'
#
# while guess_letters != guess_word:
#     x = input()
#     if x in guess_word:
#         index = guess_word.index(x)
#         guess_letters[index] = x
#         print('You did it')
#         print(guess_letters)
#
#     # store somehow this letter in guess_letters list
#     elif x not in guess_word:
#         print('Try one more time')
# if guess_letters == guess_word:
#     print('YOU WON')

