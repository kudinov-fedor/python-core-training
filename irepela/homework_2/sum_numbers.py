def sum_numbers(text: str):
    text_list = text.split()
    numbers_total = 0
    for item in text_list:
        if item.isnumeric():
            numbers_total += int(item)
    return numbers_total
