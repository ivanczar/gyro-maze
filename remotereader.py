import threading
import urllib
import requests

class RemoteReader(threading.Thread):
    def __init__(self, mazeID):
        threading.Thread.__init__(self)
        self.URL = "http://localhost/get_data.php"
        self.params = {'maze_id':mazeID}
        self.data = None

    
    def run(self):
        response = requests.get(url=self.URL, params=self.params)

        jsonData = response.json()
        print(jsonData)
        self.data = jsonData["times"]
        print(self.data)
        print(type(self.data))

        # urllib.request.urlopen("http://localhost/add_data.php?maze_id="+strMazeID+"&time="+strTime).read()
