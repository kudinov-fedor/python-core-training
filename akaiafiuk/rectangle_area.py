"""
As the input data you will get the multiline string consists of '0' & '#'. where '0' means
the empty piece of the ground and the '#' is the piece of your house.
Your task is to count the minimal area of the rectangle ground which is enough for the building.
"""


def house_area(house: str) -> int:
    # Strip the string, remove spaces and split into a list
    rows = house.strip().replace(" ", "").split('\n')
    # Get width
    widths = list()
    for row in rows:
        widths.extend(i for i, x in enumerate(row) if x == "#")
    width = max(widths) - min(widths) + 1
    # Get height
    height_indexes = [i for i, x in enumerate(rows) if '#' in x]
    height = max(height_indexes) - min(height_indexes) + 1
    return height * width
