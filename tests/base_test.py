
from src.Helpers.helperDB import HelperDB
from src.DAO.connectDB import ConnectDB
from src.SQL_Statements.SQL_Statements import SqlStatements

import pytest

class BaseTest:
    db_helper: HelperDB
    connectDB: ConnectDB
    sql: SqlStatements

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.db_helper = HelperDB()
        request.cls.connectDB = ConnectDB()
        request.cls.sql = SqlStatements()


