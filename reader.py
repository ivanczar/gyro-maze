from sqlitereader import SQLiteReader
from time import sleep
from gi.repository import GLib

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
        
    def check_thread(self, thread):
        if thread.is_alive():
            self.check_thread()