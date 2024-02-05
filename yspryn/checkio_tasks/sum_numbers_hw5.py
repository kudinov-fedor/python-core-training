# In a given text you need to sum the numbers while
# excluding any digits that form part of a word.

def sum_numbers(text: str) -> int:
    res = 0
    for i in text.split():
        if i.isnumeric():
            res += int(i)
    return res


def sum_numbers2(text: str) -> int:
    return sum(int(i) for i in text.split() if i.isnumeric())
