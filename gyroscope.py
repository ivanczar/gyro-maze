import threading

THRESH = 15
class Gyroscope(threading.Thread):

    def __init__(self , sensehat):
        threading.Thread.__init__(self)
        self.s = sensehat
        self.direction = None
        self.pitch = None
        self.roll= None
    
    def run(self):
        while True:
            o = self.s.get_orientation_degrees()
            vertical = o["roll"]
            self.roll = vertical
            horizontal = o["pitch"]
            self.pitch = horizontal

            if vertical >= (0 + THRESH) and vertical <= 180.0:
                self.direction = "S"
            elif vertical <= (360 - THRESH) and vertical >= 180.0:
                self.direction = "N"
            elif horizontal >= (0 + THRESH) and horizontal <=90.0:
                self.direction = "W"
            elif horizontal <= (360 - THRESH) and horizontal >=276.0:
                self.direction = "E"
            else:
                self.direction = None
