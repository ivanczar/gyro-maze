from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

yellow = (255, 255, 0)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)

def maze_1():
    R = red
    Y = yellow
    W = white
    O = nothing
    logo = [
    W, O, R, W, W, O, W, W,
    W, O, O, O, W, O, W, O,
    W, W, W, W, W, W, W, W,
    O, O, O, W, O, O, O, W,
    W, W, O, W, O, W, O, W,
    W, O, W, W, W, W, W, O,
    W, O, W, O, O, O, W, O,
    W, W, W, O, Y, W, W, O,
    ]
    return logo


mazes = [maze_1]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
