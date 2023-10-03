import time
import threading
class Timer():

    def __init__(self):
        
        self._start_time = None



    def start(self):

        self._start_time = time.perf_counter()


    def stop(self):

        elapsed_time = time.perf_counter() - self._start_time

        self._start_time = None
        return elapsed_time
