
from tests.base_test import BaseTest

import pytest
import logging as log


@pytest.mark.db1
class TestConnectionDB(BaseTest):

    @pytest.mark.db2
    def test_checkDB_connection_1(self):
        result = self.get_db_user.random_email_from_DB(1)
        # import pdb; pdb.set_trace()
        log.debug(result[0])
        assert result[0]['group'] == 'APG777', f"Error"

    @pytest.mark.db3
    def test_checkDB_connection(self):
        # result = self.get_db_user.random_email_from_DB(1)

        import pdb; pdb.set_trace()
        # assert result[0]['group']=='APG777', f"Error"



