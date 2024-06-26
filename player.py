


class Player:
    def __init__(self , maze, gyro):
        self.maze = maze
        self.gyro = gyro
              
        self.position = self.maze.startPos
        self.speed = 1

    def convert2Dpos(self, x, y):
        return x + (y*8)


    def canMove(self, pos):
        if pos >= 0 and pos <=63:
            return self.maze.maze[pos] == (0,0,0) or self.maze.maze[pos] == (255, 255, 0)
        else:
            return False


    def move(self):
        if (self.speed > 0):
            #print("DIRECTION:", self.gyro.direction)
            if (self.gyro.direction == "N"):
                newPos = self.convert2Dpos(self.position[0], self.position[1] - 1)
                if self.canMove(newPos):
                    self.position = (self.position[0], self.position[1] - 1)

            elif (self.gyro.direction == "S"):
                newPos = self.convert2Dpos(self.position[0], self.position[1] + 1)
                if self.canMove(newPos):
                    self.position = (self.position[0], self.position[1] + 1)


            elif (self.gyro.direction == "E"):
                newPos = self.convert2Dpos(self.position[0] + 1, self.position[1])
                if self.canMove(newPos):
                    self.position = (self.position[0] + 1, self.position[1])

            elif (self.gyro.direction == "W"):
                newPos = self.convert2Dpos(self.position[0] - 1, self.position[1])
                if self.canMove(newPos):
                    self.position = (self.position[0] - 1, self.position[1])



