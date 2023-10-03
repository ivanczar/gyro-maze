from player import Player
from sense_hat import SenseHat
from maze import Maze
from time import sleep
class Game:

    def __init__(self):
        self.s = SenseHat()
        self.maze = Maze()
        self.player = Player(self.maze, self.s)

        self.drawLED()


    def isWin(self):
        return self.player.position == self.maze.endPos


    def drawLED(self):
        print("drawing maze")
        isPlaying = True
        while isPlaying:
            isPlaying = not self.isWin()
            self.s.set_pixels(self.maze.maze)
            self.s.set_pixel(self.player.position[0], self.player.position[1], (255, 0, 0))
            sleep(1)
            self.player.move()
        print("YOU WIN!!!")

        
if __name__ == '__main__':
    game = Game()