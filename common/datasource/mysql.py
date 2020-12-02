import mysql.connector as sql

class MySqlSource:
    db = None;
    user = None;
    password = None;
    host = None;

    config = None;

    def __init__(self, config):
        self.db = config["db"]
        self.user = config["user"]
        self.password = config["password"]
        self.host = config["host"]
        self.config = config

    def sql(self, sql_string):
        cnx = sql.connect(**self.config)
        cursor = cnx.cursor()
        cursor.execute(sql_string)
        cursor.close()
        cnx.close()