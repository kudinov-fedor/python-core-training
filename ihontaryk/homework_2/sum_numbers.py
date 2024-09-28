def sum_numbers(text):
    """
    sum_numbers function
    sums the integer numbers in the text
    """

    if type(text) is not str:
        raise TypeError

    if text == '':
        raise ValueError

    words = text.split(' ')

    total = sum(int(word) for word in words if word.isdecimal())

    return total

