class Player:
    def __init__(self , starting_pos = [0,0]):
        self.position = starting_pos
        self.direction = ""
        self.speed = 0
        self.acceleration = 0

    
    def getSpeed(self):
        return self.speed   
        
    def setSpeed(self, newSpeed):
       self.speed = newSpeed 

    def getAcceleration(self):
      return self.acceleration 

    def setAcceleration(self, newAcceleration):
       self.acceleration = acceleration 

    def getDirection(self):
      return self.direction 

    def setDirection(self, newDirection):
       self.direction = newDirection 

    def getPosition(self):
       return self.position 

    def setPosition(self, x, y):
       self.position = [x,y] 

    def checkForWalls(self):
        #check for walls and bounds of led matrix (i.e 8)
        pass

    def move(self):
        if (getAcceleration > 0):
            match (getDirection()):
                case "N":
                    #checkForWalls
                    setPosition()

                case "S":
                    #checkForWalls
                    setPosition()
                
                case "E":
                    #checkForWalls
                    setPosition()

                case "W":
                    #checkForWalls
                    setPosition()



