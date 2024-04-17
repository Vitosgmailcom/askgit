
from tests.base_test import BaseTest

import pytest
import logging as log


@pytest.mark.db1
class TestConnectionDB(BaseTest):

    @pytest.mark.db2
    def test_checkDB_connection_1(self):
        result = self.db_helper.random_email_from_DB(1, self.sql.random_user_sql())
        log.info(result[0])
        assert result[0]['group'] == 'APG777', f"Error"

    @pytest.mark.db3
    def test_checkDB_connection(self):
        pass






