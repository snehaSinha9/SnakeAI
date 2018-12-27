import numpy as np
import random
import math
import SnakeGUI

class Food():

    def __init__(self):
        posX = 400 + math.floor(random.randrange(0,49)) *10
        posY = math.floor(random.randrange(0,49)) *10

        pos = np.array([posX, posY])

    def show(self):
        SnakeGUI.my_gui.canvas.create_rectangle(0,0,1,1)