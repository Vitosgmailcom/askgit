import logging as log
import pytest

@pytest.mark.health
def test_healthcheck():
    log.info("Hello world")

