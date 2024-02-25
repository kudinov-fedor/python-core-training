"""
You have to divide all your crew members into 2 teams with the next rules:
those who are elder than 40 y.o. or younger than 20, should be on the first ship
and all the others - on the second.
"""


def two_teams(sailors):
    return []


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'],
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
            ]

    assert two_teams({
        'Fernandes': 20,
        'Kale': 19.9,
        'Johnson': 40.1,
        'McCortney': 40}) == [['Johnson', 'Kale'],
                              ['Fernandes', 'McCortney']]
    print("Coding complete? Click 'Check' to earn cool rewards!")
