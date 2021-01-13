from pymongo import MongoClient
import pandas as pd
import urllib.parse
import json

class MongoDBSource:
    config = None;

    def __init__(self, config):
        self.config = config

    def _connect_mongo(self, collection):
        conn = MongoClient(self._get_uri(collection))
        return conn[self.config['db']]

    def _get_uri(self, collection):
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s.%s' % (
        urllib.parse.quote_plus(self.config['user']), urllib.parse.quote_plus(self.config['password']),
            self.config['host'], self.config['port'], self.config['db'], collection)
        if 'options' in self.config.keys():
            mongo_uri += '?'
            options = self.config["options"]
            options_list = []
            for key in options:
                options_list.append(key + "=" + options[key])
            options_str = '&'
            options_str = options_str.join(options_list)
            mongo_uri += options_str
        return mongo_uri

    def get_df(self, query, collection):
        # Connect to MongoDB
        db = self._connect_mongo(collection)
        # Make a query to the specific DB and Collection
        cursor = db[collection].find(query)
        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))
        return df

    def get_spark_df(self, spark, query, collection):
        mongo_uri = self._get_uri(collection)
        spark.read.format("mongo").option("uri", mongo_uri).option("pipeline", query).load()