def sum_numbers(text: str):
    return sum(int(word) for word in text.split() if word.isdigit())
