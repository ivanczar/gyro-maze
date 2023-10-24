from sqlitereader import SQLiteReader
from time import sleep
from gi.repository import GLib
from remotereader import RemoteReader

class Reader():
    def __init__(self):
        pass
    

    def readLocal(self, mazeID):
        reader = SQLiteReader(mazeID)
        reader.start()

        while reader.is_alive():
            pass
        
        time = reader.data
        return time
        
        
    def readRemote(self, mazeID):
        reader = RemoteReader(mazeID)
        reader.start()

        while reader.is_alive():
            pass

        time = reader.data
        print("TIME: ", time)
        return time