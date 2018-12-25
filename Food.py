import numpy as np
import random
import math
import SnakeGUI

class Food(object):
    __metaclass__ = SnakeGUI
    def __init__(self):
        posX = 400 + math.floor(random.randrange(0,49)) *10
        posY = math.floor(random.randrange(0,49)) *10

        pos = np.array([posX, posY])

    def show(self, master):
        self.create_line(0,0,200,100)