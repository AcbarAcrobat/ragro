import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.sub_suite("/host/search/start_unload")
@allure.title("Positive post request")
def test_host_search_start_unload():
    with allure.step("Send request to the server"):
        r = requests.post(T.url() + "/host/search/start_unload", headers=T.headers())
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
