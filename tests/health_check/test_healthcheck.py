import logging as log
import pytest

@pytest.mark.health
def test_healthcheck():
    """
    Check the health of the system.

    :return: None
    """
    log.info("Hello world")

