
from src.DAO.connectDB import ConnectDB

import random

class HelperDB(ConnectDB):
    def random_email_from_DB(self, qty, sql):
        if not qty:
            qty = 1
        exec = self.execute_SELECT(sql)
        return random.sample(exec, qty)

    def get_existing_user(self):
        pass

    def add_user_to_db(self):
        pass

    def get_activation_code(self):
        pass



