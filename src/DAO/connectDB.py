

from src.Utility.credentialsDB import Credentials

import logging
import pymysql.cursors
import logging as log

class ConnectDB(object):

    def __init__(self):
        self.cred = Credentials()
        self.port = int(self.cred['db_port'])
    def connect(self):
        connection = pymysql.connect(
            user=self.cred['db_user'],
            password=self.cred['db_pass'],
            database=self.cred['db_name'],
            port=self.port,
            host=self.cred['db_host']
            )

        return connection

    def execute_SELECT(self, sql):
        conn =self.connect()
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            cursor.execute(sql)
            result = cursor.fetchall()

            return result


