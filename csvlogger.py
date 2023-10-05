import threading
from csv import writer

class CSVLogger(threading.Thread):
    def __init__(self,time, posx,posy,dir, pitch, roll):
        threading.Thread.__init__(self)
        self.posx = str(posx)
        self.posy = str(posy)
        self.dir = str(dir)
        self.time = str(time)
        self.pitch = str(pitch)
        self.roll = str(roll)

    
    def run(self):
        with open('movement.csv', 'a') as f:
            data_writer = writer(f)
            data_writer.writerow([self.time, self.posx, self.posy, self.dir, self.pitch, self.roll])

