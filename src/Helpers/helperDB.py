
from src.DAO.connectDB import ConnectDB

import random

class HelperDB(ConnectDB):
    # def __init__(self):
    #     self.conn = ConnectDB()

    def random_email_from_DB(self, qty):
        if not qty:
            qty = 1
        sql = f"SELECT * FROM users WHERE `group`='APG777' order by id ASC LIMIT 10;"

        exec = self.execute_SELECT(sql)
        return random.sample(exec, qty)

