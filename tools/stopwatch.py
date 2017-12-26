import datetime


class Stopwatch(object):

    def __init__(self):
        pass

    def start(self):
        self.start = datetime.datetime.now()
        return self.start

    def stop(self, message="Total: "):
        self.stop = datetime.datetime.now()
        return message + str(self.stop - self.start)

    @staticmethod
    def now(message="Now: "):
        return message + ": " + str(datetime.datetime.now())

    def elapsed(self, message="Elapsed: "):
        return message + str(datetime.datetime.now() - self.start)

    def split(self, message="Split started at: "):
        self.split_start = datetime.datetime.now()
        return message + str(self.split_start)

    def unsplit(self, message="Unsplit: "):
        return message + str(datetime.datetime.now() - self.split_start)
