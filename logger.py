from csvlogger import CSVLogger
from sqlitelogger import SQLiteLogger
from remotelogger import RemoteLogger

class Logger():
    def __init__(self):
        pass
    

    def logCSV(self,time, posx,posy,dir, pitch, roll):
        logger = CSVLogger( time, posx,posy,dir, pitch, roll)
        logger.start()
    
    def saveLocal(self, endPos, mazeID):
        saver = SQLiteLogger(endPos, mazeID)
        saver.start()
        