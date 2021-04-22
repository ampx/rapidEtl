from datetime import datetime

from util import util

class Bookmark:
    timestamp = None
    metrics = None
    def __init__(self, metrics = {}):
        self.timestamp = datetime.now()
        self.metrics = metrics

    def toDict(self):
        return {"timestamp": {"instant": util.datetime_to_json(self.timestamp)}, "metrics": self.metrics}

failed = 2
locked = 1
unlocked = 0