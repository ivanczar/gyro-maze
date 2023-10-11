import threading
from csv import reader
import sqlite3

class SQLiteReader(threading.Thread):
    def __init__(self, mazeID):
        threading.Thread.__init__(self)
        self.data = None
        self.mazeID = mazeID

    
    def run(self):
        conn = sqlite3.connect("GyroMaze.db")
        c = conn.cursor()
        query = "SELECT time FROM gametimes WHERE maze_id = ? ORDER BY time ASC LIMIT 1"
        c.execute(query, (self.mazeID))
        result = c.fetchone()
        rounded = "{:.3f}".format(result[0])
        print(rounded)
        self.data = rounded
        

        