import allure
import requests
from truth.truth import AssertThat
import support.test_data2 as TD
import logging

LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.sub_suite("/host/guest/start_unload")
@allure.title("Positive post request")
def test_guest_start_unload():
    pass
