from pymongo import MongoClient
import pandas as pd

class MongoDBSource:
    config = None;

    def __init__(self, config):
        self.config = config

    def _connect_mongo(self):
        if 'username' in self.config.keys():
            mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (self.config['username'], self.config['password'], self.config['host'], self.config['port'], self.config['db'])
            if 'config' in self.config.keys():
                mongo_uri+='?'
                config = self.config["config"]
                for key in config:
                    mongo_uri +='&'+key+"="+config[key]
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(self.config['host'], self.config['port'])
        return conn[self.config['db']]

    def get_df(self, query, collection):
        # Connect to MongoDB
        db = self._connect_mongo()
        # Make a query to the specific DB and Collection
        cursor = db[collection].find(query)
        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))
        return df

    def get_spark_df(self, spark, query, collection):
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s.%s' % (
        self.config['username'], self.config['password'], self.config['host'], self.config['port'], self.config['db'],
                        collection)
        if 'config' in self.config.keys():
            mongo_uri += '?'
            config = self.config["config"]
            for key in config:
                mongo_uri += '&' + key + "=" + config[key]
        spark.read.format("mongo").option("uri", mongo_uri).option("pipeline", query).load()