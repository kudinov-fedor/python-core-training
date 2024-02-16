def max_function(*items, key=None):
    minimum_value = 0
    for item in list(items):
        for number in item:
            if number > minimum_value:
                minimum_value = number
            else:
                pass
        return minimum_value
