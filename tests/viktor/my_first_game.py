#
# print('Welcome to my first game "Guess the word"')
#
# print("Enter your first guess letter:")
# x = input()
# print(x)
#
# guess_word = ['python']
#
# guess_letters = ['******']
#
# while guess_letters != guess_word:
#     if x in guess_word:
#         index = guess_word.index(x)
#         guess_letters[index] = x
#         print('You did it')
#         print(guess_letters)
#     # store somehow this letter in guess_letters list
#     elif x not in guess_word:
#         print('Try one more time')
#



print('Welcome to my first game "Guess the word"')

print("Enter your first guess letter:")
x = input()
print(x)

guess_word = ['p', 'y', 't', 'h', 'o', 'n']

guess_letters = ['*', '*', '*', '*', '*', '*']

while guess_letters != guess_word:
    if x in guess_word:
        index = guess_word.index(x)
        guess_letters[index] = x
        print('You did it')
        print(guess_letters)
    # store somehow this letter in guess_letters list
    elif x not in guess_word:
        print('Try one more time')
        break

