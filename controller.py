from game import Game
from sense_hat import SenseHat
from joystick import Joystick
from gyroscope import Gyroscope

class Controller:
    def __init__(self):
        self.s = SenseHat()
        self.joystick = Joystick(self.s)
        self.joystick.start()
        self.gyroscope = Gyroscope(self.s)
        self.gyroscope.start()  
        self.game = Game(self.s, self.gyroscope)
        self.game.start()
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

                    

    def generateNewMaze(self):
        self.game.isPlaying = False
        print("NEW GAME MADE")
        self.game = Game(self.s, self.gyroscope)
        self.game.start()
    
    def resetPlayer(self):
        self.game.reset()


if __name__ == '__main__':
    controller = Controller()

    