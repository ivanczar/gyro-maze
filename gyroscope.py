import threading
class Gyroscope(threading.Thread):
    def __init__(self , sensehat):
        threading.Thread.__init__(self)
        self.s = sensehat
        self.direction = "N"
    
    def run(self):
        while True:
            o = self.s.get_orientation_degrees()
            vertical = o["roll"]
            horizontal = o["pitch"]

            if vertical >= 10.0 and vertical <= 180.0:
                self.direction = "S"
            elif vertical <= 350 and vertical >= 180.0:
                self.direction = "N"
            elif horizontal >= 10.0 and horizontal <=90.0:
                self.direction = "W"
            elif horizontal <= 350.0 and horizontal >=276.0:
                self.direction = "E"



