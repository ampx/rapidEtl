from datetime import datetime

from util import util


class Bookmark:
    timestamp = None
    metrics = None

    def __init__(self, metrics={}, timestamp=datetime.now()):
        self.timestamp = timestamp
        self.metrics = metrics

    def toDict(self):
        return {"timestamp": {"instant": util.datetime_to_json(self.timestamp)}, "metrics": self.metrics}
