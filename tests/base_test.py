import pytest

from src.Helpers.helperDB import HelperDB
from src.DAO.connectDB import ConnectDB

class BaseTest:
    get_db_user: HelperDB
    connectDB: ConnectDB



    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.get_db_user = HelperDB()
        request.cls.connectDB = ConnectDB()

