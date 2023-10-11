import time
import threading
class Timer():
    def __init__(self):
        self._start_time = None

    def lap(self):
        return time.perf_counter() - self._start_time


    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is not None:
            elapsed_time = time.perf_counter() - self._start_time
            self._start_time = None
        else:
            elapsed_time = 0
        return elapsed_time

    def reset(self):
        self.stop()
        self.start()

