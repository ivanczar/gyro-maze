from sense_hat import SenseHat
import time

yellow = (255, 255, 0)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
R = red
Y = yellow
W = white
O = nothing
class Maze():

    def __init__(self):
        self.maze, self.startPos, self.endPos = self.generateMaze()
        

# s.low_light = True

    def generateMaze(self):
        startPos = (2,0)
        endPos = (4,7)

        print("maze generated")
        maze_1 = [
        O, W, O, O, O, W, O, O,
        O, W, W, W, O, W, O, W,
        O, O, O, O, O, O, O, O,
        W, W, W, O, W, W, W, O,
        O, O, W, O, W, O, W, O,
        O, W, O, O, O, O, O, W,
        O, W, O, W, W, W, O, W,
        O, O, O, W, Y, O, O, W,
        ]
        return maze_1, startPos, endPos




