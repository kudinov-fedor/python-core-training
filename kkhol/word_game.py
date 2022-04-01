word = 'apple'

print('The word you are to guess is: "Fruit that is also a piece of technology". \n'
      'There are', len(word), 'letters.')

used = []

display = '_' * len(word)

print(" ".join(display))

while display != word:
    letter = input('What is your guess?')
    used.extend(letter)
    for i in range(len(word)):

        if letter and letter == word[i]:
            display = display[0:i] + letter + display[i + 1:]
            print(letter,' is correct,')

    print('You already tried:',set(used))

    print(" ".join(display))

print('Congratulations! The word was', word)
