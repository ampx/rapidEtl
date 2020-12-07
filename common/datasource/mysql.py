import mysql.connector as sql
import pandas as pd

class MySqlSource:
    config = None;

    def __init__(self, config):
        self.config = config

    def sql(self, sql_string):
        cnx = self.create_connection()
        cursor = cnx.cursor()
        cursor.execute(sql_string)
        cursor.close()
        cnx.close()
        #self.create_engine().execute(sql_string)

    def duplicate_update(self, df, table_name, sum_fields=[], append_fields=[], overwrite_nulls=[]):
        engine = self.create_connection()
        temp_table = table_name + '_temp_df'
        df.to_sql(con=engine, name=temp_table, if_exists='append')
        self.duplicate_update_subquery(table_name, 'Select * from '+temp_table,
                                       sum_fields, append_fields, overwrite_nulls)
        engine.execute('DROP TABLE ' + temp_table)

    def duplicate_update_subquery(self, table_name, subquery, sum_fields=[], append_fields=[], overwrite_nulls=[]):
        sql_update = 'INSERT INTO ' + table_name + ' ' + subquery + ' as subquery '
        sql_update += 'ON DUPLICATE KEY UPDATE '
        for sum_field in sum_fields:
            sql_update += table_name + '.' + sum_field + '=' + \
                          table_name + '.' + sum_field + '+subquery.' + sum_field + ','
        for append_field in append_fields:
            sql_update += table_name + '.' + append_field + '=' + \
                          table_name + '.' + append_field + '+ 1,'
        for overwrite_null in overwrite_nulls:
            sql_update += table_name + '.' + overwrite_null + '=' + \
                          'if(' + table_name + '.' + overwrite_null + ' is NULL ,' + \
                          'subquery.' + overwrite_null + ',' + \
                          table_name + '.' + overwrite_null + '),'
        self.sql(sql_update.rstrip(','))

    def insert_df(self, df, table_name):
        df.to_sql(con=self.create_connection(), name=table_name, if_exists='append')

    def create_connection(self):
        return sql.connect(**self.config)

    def get_df(self, query):
        return pd.read_sql(query, self.create_connection())

    #def create_engine(self):
    #    url = 'mysql://' + self.config['user'] + ':' + self.config['password'] \
    #                     + '@' + self.config['host']
    #    if 'port' in self.config:
    #        url += ':' + str(self.config['port'])
    #    url += '/' + self.config['db']
    #    for key, value in self.config.items():
    #        if key not in ['user', 'password', 'host', 'port', 'db']:
    #            url += '?' + key + '=' + value
    #    return create_engine(url)
