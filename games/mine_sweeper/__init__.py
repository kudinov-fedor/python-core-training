# minesweeper

height, width = 10, 7
mines = [(5, 7), (3, 9), (5, 5)]
deltas = [(1, 0), (-1, 0), (0, 1), (0, -1),
          (1, 1), (-1, 1), (1, -1), (-1, -1)]

# setup
field = [["."] * width for _ in range(height)]

# display
for i in field:
    print(i)
print("-" * width)


# -------- step -------------
# act
guess = 5, 6

# count mines
mines_around = sum((guess[0] + dx, guess[1] + dy) in mines for dx, dy in deltas)

# set sign
sign = "*" if guess in mines else str(mines_around)
field[guess[1]][guess[0]] = sign

# display
for i in field:
    print(i)
print("-" * width)


# -------- step -------------
# act
guess = 5, 5

# count mines
mines_around = sum((guess[0] + dx, guess[1] + dy) in mines for dx, dy in deltas)

# set sign
sign = "*" if guess in mines else str(mines_around)
field[guess[1]][guess[0]] = sign

# display
for i in field:
    print(i)
print("-" * width)
