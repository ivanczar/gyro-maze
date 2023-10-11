from player import Player
from maze import Maze
from time import sleep
from timer import Timer
from logger import Logger
import threading

class Game(threading.Thread):

    def __init__(self, sensehat, gyroscope, ):
        threading.Thread.__init__(self)
        self.s = sensehat
        self.maze = Maze()
        self.player = Player(self.maze, gyroscope)
        #self.joystick = Joystick(self.s)
        self.timer = Timer()
        self.logger = Logger()
        self.isPlaying = False
        self.hasFinished = False

        
        

    def isWin(self):
        return self.player.position == self.maze.endPos

    def drawLED(self):
        self.s.set_pixels(self.maze.maze)
        self.s.set_pixel(self.player.position[0], self.player.position[1], (255, 0, 0))
        sleep(0.5)
        self.player.move()
       
    def reset(self):
        self.player.position = self.maze.startPos
        self.timer.reset()


    def run(self):    
        self.timer.start()
        
        self.isPlaying = True

        while self.isPlaying:
            self.isPlaying = not self.isWin()
            self.drawLED()
            self.logger.logCSV(self.timer.lap() , self.player.position[0],self.player.position[1], self.player.gyro.direction,  self.player.gyro.pitch, self.player.gyro.roll)
            self.hasFinished = self.isWin()

        if self.hasFinished:
            finishTime = self.timer.stop()
            print("YOU WIN in ", finishTime)
            
            self.logger.saveLocal(self.maze.endPos)
        return
        
