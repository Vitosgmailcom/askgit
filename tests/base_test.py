
from src.Helpers.helperDB import HelperDB
from src.DAO.connectDB import ConnectDB
from src.SQL_Statements.SQL_Statements import SqlStatements

import pytest

class BaseTest:
    """
    Sets up the necessary fixtures for the test.

    :param request: The test request object from pytest.
    :type request: _pytest.fixtures.FixtureRequest
    """
    db_helper: HelperDB
    connectDB: ConnectDB
    sql: SqlStatements

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.db_helper = HelperDB()
        request.cls.connectDB = ConnectDB()
        request.cls.sql = SqlStatements()


