from pymongo import MongoClient
import pandas as pd

class MongoDBSource:
    config = None;

    def __init__(self, config):
        self.config = config

    def _connect_mongo(self):
        if 'username' in self.config.keys():
            mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (self.config['username'], self.config['password'], self.config['host'], self.config['port'], self.config['db'])
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(self.config['host'], self.config['port'])

        return conn[self.config['db']]

    def read_mongo(self, query, collection):

        # Connect to MongoDB
        db = self._connect_mongo()

        # Make a query to the specific DB and Collection
        cursor = db[collection].find(query)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))

        return df

