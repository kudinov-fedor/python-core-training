word = 'apple'
print('The word you are to guess is: "Fruit that is also a piece of technology". \n'
      'There are', len(word), 'letters.')
used = []
display = word
for i in range(len(word)):
    # replace each letter with a '_'
    display = display[0:i] + "_" + display[i + 1:]

print(" ".join(display))

typed_letter = 0

while typed_letter < len(word):
    letter = input('What is your guess?')
    used.extend(letter)

    for i in range(len(word)):
        if letter and letter == word[i]:
            display = display[0:i] + letter + display[i + 1:]
            print('Correct,', letter, 'is under index', word.index(letter))
            typed_letter = typed_letter + 1
        #else:
            #print('No such letter')
    print('You already tried:', used)

    print(" ".join(display))

print('Congratulations! The word was', word)