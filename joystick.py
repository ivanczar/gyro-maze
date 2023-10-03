import threading
class Joystick(threading.Thread):
    def __init__(self,sense):
        threading.Thread.__init__(self)
        self.s = sense
        self.joyDir = None
        
        
    def run(self):
        while True:
            for event in self.s.stick.get_events():
                if event.action == "pressed":
                    self.joyDir = event.direction
                    print("DIR: ", self.joyDir)
                else:
                    self.joyDir = None