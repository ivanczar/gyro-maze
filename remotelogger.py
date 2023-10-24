import threading
import urllib
import requests

class RemoteLogger(threading.Thread):
    def __init__(self, mazeID, time):
        threading.Thread.__init__(self)
        self.URL = "http://localhost/add_data.php"
        self.data = {'maze_id':mazeID,'times':time}

    
    def run(self):
        requests.get(url=self.URL, params=self.data)
        # urllib.request.urlopen("http://localhost/add_data.php?maze_id="+strMazeID+"&time="+strTime).read()
