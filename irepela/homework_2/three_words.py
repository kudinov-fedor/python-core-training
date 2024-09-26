def checkio(words: str):
    counter = 0
    word_list = words.split()
    for word in word_list:
        if word.isnumeric():
            counter = 0
        else:
            counter += 1
        if counter == 3:
            break
    return counter == 3
