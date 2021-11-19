# snake

orientation = (0, -1)
snake = [(2, 2), (2, 2), (2, 2), (2, 2), (2, 2)]
size = 5


# ------- turn ---------
orientation = (0, -1)  # act

#  move snake
next_move = snake[0][0] + orientation[0], snake[0][1] + orientation[1]

snake.insert(0, next_move)
if len(snake) > size:
    snake.pop(-1)

# show
print(snake)


# ------- turn ---------
orientation = (1, 0)  # act

#  move snake
next_move = snake[0][0] + orientation[0], snake[0][1] + orientation[1]

snake.insert(0, next_move)
if len(snake) > size:
    snake.pop(-1)

# show
print(snake)
