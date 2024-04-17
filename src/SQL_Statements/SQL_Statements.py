
class SqlStatements:
    def random_user_sql(self):
        return f"SELECT * FROM users WHERE `group`='APG777' order by id ASC LIMIT 10;"

    def specific_user_sql(self, email):
        return f"SELECT * FROM users WHERE `email`='{email}';"

