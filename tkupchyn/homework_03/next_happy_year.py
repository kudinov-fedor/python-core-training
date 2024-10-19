""""
You're saying goodbye your best friend , See you next happy year .
Happy Year is the year with only distinct digits , (e.g) 2018

Given a year, Find The next happy year or The closest year You'll see your best friend

Year Of Course always Positive .
Have no fear , It is guaranteed that the answer exists .
It's not necessary that the year passed to the function is Happy one .
Input Year with in range (1000 ≤ y ≤ 9000)

nextHappyYear (7712) ==> return (7801)
"""


def next_happy_year(year: int) -> int:
    """
    Function finds the closest next happy year.

    Args:
        year (int): Year with in range (1000 ≤ y ≤ 9000)

    Returns:
        int: Return the next happy year.
    """

    if year not in range(1000, 9001):
        raise ValueError(f"Year {year} is out of range")

    is_happy_year = None

    while not is_happy_year:
        year_str = str(year)

        if any([digit for digit in year_str if year_str.count(digit) > 1]):
            is_happy_year = False
            year += 1
        else:
            if is_happy_year is None:
                is_happy_year = False
                year += 1
                continue
            else:
                is_happy_year = True

    return year


def is_happy_year(year):
    return len(set(str(year))) == 4


def next_happy_year_alternative(year: int) -> int:
    if year not in range(1000, 9001):
        raise ValueError(f"Year {year} is out of range")

    year = year + 1 if is_happy_year(year) else year

    while not is_happy_year(year):
        year += 1

    return year
