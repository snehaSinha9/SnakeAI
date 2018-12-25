from tkinter import *
import Food

class SnakeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Snake Game")
        master.grid()
        
        self.canvas = Canvas(master, width = 1200, height = 400, bg = "green")
        self.canvas.pack(side = RIGHT)

        self.label_points = Label(master, text = "POINTS: ")
        self.label_points.pack(side = TOP)

        self.play_button = Button(master, text="Play", command=self.play)
        self.play_button.pack(side = LEFT)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side= LEFT)

        self.play()


    def play(self):
        print("Play in progress.")

        self.canvas.delete(ALL)
        food = Food(self.master)


root = Tk()
my_gui = SnakeGUI(root)
root.mainloop()