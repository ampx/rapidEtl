from pyspark.sql import SparkSession

class SparkSource:
    config = None;

    def __init__(self, config):
        self.config = config

    def get_spark(self, appName):
        spark = None;
        if "master_ip" in self.config:
            master_ip=self.config["master_ip"]
            if "master_port" in self.config:
                master_port=self.config["master_port"]
            else:
                master_port=7077
            spark = SparkSession.builder\
                .master("spark://"+str(master_ip)+":"+str(master_port))\
                .appName(appName).getOrCreate()
        else:
            spark = SparkSession.builder.appName(appName).getOrCreate()
        return spark