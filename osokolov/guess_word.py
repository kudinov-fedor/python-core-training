import re


def guess(word, hint):
    print('Welcome!')
    guessing_word = ['_ '] * len(word)
    print(f'Guessed word is the {hint}: {"".join(guessing_word)}')
    print('If you want ot quit the game input q')
    while True:
        print("".join(guessing_word))
        answer = input('Your try: ').lower()
        if "".join(guessing_word) == word:
            print(f'You guess!\nIt is: {word}')
            break
        elif answer == 'q':
            break
        elif len(answer) > 1 or re.search(r'[^a-z]', answer) is not None:
            continue
        elif answer not in word:
            print('This letter is not in the word')
            continue
        elif answer in word:
            for i in range(len(word)):
                if word[i] == answer:
                    guessing_word[i] = answer
            continue
        else:
            break
