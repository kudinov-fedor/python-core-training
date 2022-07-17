import re


def guess(word: str, hint: str):
    print('Welcome!')
    guessing_word = ['_ '] * len(word)
    print(f'Guessed word is the {hint}: {"".join(guessing_word)}')
    print('If you want ot quit the game input word: quit')
    while True:
        print("".join(guessing_word))
        answer = input('Your try: ').lower()
        if "".join(guessing_word) == word:
            print(f'You guess!\nIt is: {word}')
            break
        elif answer == 'quit':
            break
        elif len(answer) > 1 or re.search(r'[a-z]', answer) is None:
            print('Input correct data')
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
