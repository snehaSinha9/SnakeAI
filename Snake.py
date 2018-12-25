import numpy as np

class Snake:
    length = 1
    posX = 0
    posY = 0

    head = np.array([posX, posY])
    tail = []

    velocity = np.array([0,0])

    temp = np.array()

    food = Food()