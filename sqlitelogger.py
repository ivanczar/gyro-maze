import threading
from csv import reader
import sqlite3
import os

class SQLiteLogger(threading.Thread):
    def __init__(self, endPos):
        threading.Thread.__init__(self, )
        self.endPos = endPos
        

    
    def run(self):
        conn = sqlite3.connect("GyroMaze.db")
        c = conn.cursor()
        createTable = "CREATE TABLE IF NOT EXISTS gamedata(time REAL, position TEXT, direction TEXT, pitch REAL, roll REAL)"
        c.execute(createTable)
        conn.commit()

        endTime = None

        with open('movement.csv', newline='') as f:
            data_reader = reader(f, delimiter=',')
            for row in data_reader:
                print(row)
                pos = row[1] + ',' + row[2]
                c.execute("INSERT INTO gamedata(time, position, direction, pitch, roll) VALUES(?, ?, ? , ?, ?)",
                            (float(row[0]), pos, row[3], float(row[4]), float(row[5])))
                conn.commit()
                if int(row[1]) == self.endPos[0] and int(row[2]) == self.endPos[1]:
                    endTime = float(row[0])
                    break
            print("here")

        # get current bes time form maze table
        # comare and do logic

        os.remove('movement.csv')
                

                

                


            

