import time

class Timer:
    def time(method):
        start = time.time()
        method()
        end = time.time()
        return end - start