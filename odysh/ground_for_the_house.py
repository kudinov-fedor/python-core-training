"""
As the input data you will get the multiline string consists of '0' & '#'. where '0' means
the empty piece of the ground and the '#' is the piece of your house.
Your task is to count the minimal area of the rectangle ground which is enough for the building.

Example:
house('''
    0000000
    ##00##0
    ######0
    ##00##0
    #0000#0
''') == 24
"""


def house_area(house):
    house = house.split('\n')[:-1]

    rows_to_del = ''

    # LTR
    for item in range(len(house)):
        if '#' not in house[item]:
            rows_to_del += str(item)
        elif '#' in house[item]:
            break

    # RTL
    for item in range(len(house)-1, 0, -1):
        if '#' not in house[item]:
            rows_to_del += str(item)
        elif '#' in house[item]:
            break

    house = [house[i] for i in range(len(house)) if str(i) not in rows_to_del]
    house_copy = house.copy()

    if len(house) >= 1:
        for i in range(len(house[0])):
            first_char = [x[i] for x in house_copy]
            if '#' not in first_char:
                house = [x[i+1:] for x in house_copy]
            elif '#' in first_char:
                break

        if len(house) > 0:
            for i in range(len(house[0])-1, 0, -1):
                last_char = [x[i] for x in house]
                if '#' not in last_char:
                    house = [x[:i] for x in house]
                elif '#' in last_char:
                    break
            return len(house) * len(house[0])
        else:
            for i in range(len(house[0]) - 1, 0, -1):
                last_char = [x[i] for x in house]
                if '#' not in last_char:
                    house = [x[:i] for x in house]
                elif '#' in last_char:
                    ...
            return len(house) * len(house[0])
    else:
        return 0
