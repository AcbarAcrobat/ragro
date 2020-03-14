import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.sub_suite("/host/guest/start_unload")
@allure.title("Positive post request")
def test_guest_start_unload():
    pass
