from pyspark.sql import SparkSession

class SparkSource:
    config = None;

    def __init__(self, config):
        self.config = config

    def get_spark(self, appName):
        sparkSessionBuilder = SparkSession.builder
        if "master_ip" in self.config:
            master_ip=self.config["master_ip"]
            if "master_port" in self.config:
                master_port=self.config["master_port"]
            else:
                master_port=7077
            sparkSessionBuilder = \
                sparkSessionBuilder.master("spark://"+str(master_ip)+":"+str(master_port))

        if "options" in self.config:
            options = self.config["options"]
            for key in options:
                sparkSessionBuilder = sparkSessionBuilder.config(key, options[key])

        return sparkSessionBuilder.appName(appName).getOrCreate()