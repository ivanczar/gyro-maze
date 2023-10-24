from game import Game
from sense_hat import SenseHat
from joystick import Joystick
from gyroscope import Gyroscope
from reader import Reader

class Controller:
    def __init__(self):
        self.s = SenseHat()
        self.joystick = Joystick(self.s)
        self.joystick.start()
        self.gyroscope = Gyroscope(self.s)
        self.gyroscope.start()  
        self.game = Game(self.s, self.gyroscope)
        self.game.start()
        self.reader = Reader()

        self.handleJoystick()

    def handleJoystick(self):
        while True:
            if self.joystick.joyDir is not None:
                if self.joystick.joyDir == "left":
                    print("GEN")
                    self.generateNewMaze()
                    self.joystick.joyDir = None
                if self.joystick.joyDir == "right":
                    print("reseeting player")
                    self.resetPlayer()
                    self.joystick.joyDir = None
                if self.joystick.joyDir == "down":
                    print("displaying best time")
                    bestTime = self.reader.readLocal(self.game.maze.mazeID)
                    self.game.drawBestTime("Local", bestTime)
                    self.joystick.joyDir = None
                if self.joystick.joyDir == "up":
                    print("displaying best remote time")
                    bestRemoteTime = self.reader.readRemote(self.game.maze.mazeID)
                    self.game.drawBestTime("Remote", bestRemoteTime)
                    self.joystick.joyDir = None
                    

    def generateNewMaze(self):
        self.game.isPlaying = False
        print("NEW GAME MADE")
        self.game = Game(self.s, self.gyroscope)
        self.game.start()
    
    def resetPlayer(self):
        self.game.reset()


if __name__ == '__main__':
    controller = Controller()

    