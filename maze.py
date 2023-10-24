from sense_hat import SenseHat
import time
import random

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
        self.mazes = [self.purpleMaze, self.IOMaze, self.spicyMaze]

        self.maze, self.startPos, self.endPos, self.mazeID = self.generateMaze()
        

    def generateMaze(self):
        randInt = random.randint(0,2)
        maze = self.mazes[randInt]
        return maze()


    def purpleMaze(self):
        startPos = (2,0)
        endPos = (4,7)
        mazeID = 1

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
        return maze_1, startPos, endPos, mazeID

    def IOMaze(self):
        startPos = (0,0)
        endPos = (7,7)
        mazeID = 2

        print("maze generated")
        maze_1 = [
        O, W, O, O, O, W, O, W,
        O, W, O, W, O, O, O, O,
        O, O, O, W, O, W, W, O,
        O, W, W, O, O, O, W, O,
        W, O, O, O, W, W, W, O,
        O, O, W, W, O, O, O, W,
        O, W, O, W, O, W, W, W,
        O, O, O, O, O, O, O, Y,
        ]
        return maze_1, startPos, endPos, mazeID
    
    def spicyMaze(self):
        startPos = (4,0)
        endPos = (2,7)
        mazeID = 3

        print("maze generated")
        maze_1 = [
        W, O, O, O, O, W, W, W,
        W, O, W, O, W, O, O, O,
        O, O, W, O, O, O, W, O,
        O, W, O, O, W, O, W, O,
        O, W, W, W, O, O, W, O,
        W, O, O, O, W, W, O, O,
        W, O, W, O, O, O, O, W,
        W, O, Y, W, O, W, O, O,
        ]
        return maze_1, startPos, endPos, mazeID


