from collections import deque


def answer(area):
    current_square = 0

    num = 1
    while current_square < area:
        current_square = num**2
        num += 1

    squares = list()
    while area != 0:
        num_squared = num**2
        if num_squared <= area:
            squares.append(num_squared)
            area -= num_squared
        else:
            num -= 1

    return squares
