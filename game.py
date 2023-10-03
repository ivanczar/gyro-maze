from player import Player
from sense_hat import SenseHat
from maze import Maze
from time import sleep
from timer import Timer
class Game:

    def __init__(self):
        self.s = SenseHat()
        self.maze = Maze()
        self.player = Player(self.maze, self.s)
        self.timer = Timer()
        
        self.finishTime = 0
        self.drawLED()


    def isWin(self):
        return self.player.position == self.maze.endPos


    def drawLED(self):
        print("drawing maze")
        self.timer.start()
        isPlaying = True
        while isPlaying:
            isPlaying = not self.isWin()
            self.s.set_pixels(self.maze.maze)
            self.s.set_pixel(self.player.position[0], self.player.position[1], (255, 0, 0))
            sleep(0.5)
            self.player.move()
        self.finishTime = self.timer.stop()
        print("YOU WIN in ", self.finishTime)

        
if __name__ == '__main__':
    game = Game()