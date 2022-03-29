word = 'apple'
print('The word you are to guess is: "Fruit that is also a piece of technology". \n'
      'There are', len(word), 'letters.')
typed_letter = 0
while typed_letter < len(word):
    letter = input('Great, so what is your guess?')
    if letter in word:
        print('Correct,', letter, 'is under index', word.index(letter),', and you have', word[:typed_letter + 1])
        typed_letter = typed_letter + 1
    else:
        print('There is no such letter')
print('The word was ', word)