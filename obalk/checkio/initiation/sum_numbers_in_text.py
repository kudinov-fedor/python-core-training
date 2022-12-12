def sum_numbers(text: str):
    return sum(int(word) for word in text.split() if word.isdigit())


def sum_numbers_with_filter_map(text: str):
    return sum(map(int, filter(str.isdigit, text.split())))
