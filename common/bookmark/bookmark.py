from datetime import datetime

from util import util


class Bookmark:
    timestamp = None
    metrics = None

    def __init__(self, metrics={}, timestamp=None):
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp
        self.metrics = metrics

    def toDict(self):
        return {"timestamp": {"time": util.datetime_to_json(self.timestamp)}, "metrics": self.metrics}
