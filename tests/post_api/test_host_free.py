import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST requests")
@allure.sub_suite("/host/free")
@allure.title("POSITIVE TESTS")
def test_host_free():
    with allure.step("Send request to the server"):
        r = requests.post(T.url_() + "/host/free", headers=T.headers())
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    LOGGER.info(r.json())
    LOGGER.info(r.status_code)
