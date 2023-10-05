from player import Player
from sense_hat import SenseHat
from maze import Maze
from time import sleep
from joystick import Joystick
from timer import Timer
from logger import Logger

class Game:

    def __init__(self):
        self.s = SenseHat()
        self.maze = Maze()
        self.player = Player(self.maze, self.s)
        self.joystick = Joystick(self.s)
        self.timer = Timer()
        self.logger = Logger()
        self.finishTime = 0
        self.begin()

    def isWin(self):
        return self.player.position == self.maze.endPos

    def handleJoystick(self):
        if self.joystick.joyDir is not None:
            print(self.joystick.joyDir)
            # LOG HERE

    def drawLED(self):
        self.s.set_pixels(self.maze.maze)
        self.s.set_pixel(self.player.position[0], self.player.position[1], (255, 0, 0))
        sleep(0.5)
        self.player.move()
       

    def begin(self):    
        self.timer.start()
        self.joystick.start()
        isPlaying = True

        while isPlaying:
            isPlaying = not self.isWin()
            self.drawLED()
            # log position
            self.logger.logCSV(self.timer.lap() , self.player.position[0],self.player.position[1], self.player.gyro.direction,  self.player.gyro.pitch, self.player.gyro.roll)

        self.finishTime = self.timer.stop()
        self.logger.saveLocal(self.maze.endPos)
        # LOG HERE
        print("YOU WIN in ", self.finishTime)
        return
        
if __name__ == '__main__':
    game = Game()