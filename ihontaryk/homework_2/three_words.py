def three_words(text):
    """
    three_words function
    checks if the string contains three words in succession
    """

    if type(text) is not str:
        raise TypeError

    if text == '':
        raise ValueError

    elements = text.split()

    result = []

    for element in elements:
        if element.isalpha():
            result.append(element)
        else:
            result = []

        if len(result) >= 3:
            return True
        else:
            continue

    return False

