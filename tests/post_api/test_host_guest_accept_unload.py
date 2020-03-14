import logging
import allure
import requests
from support.testdata import TestData
from truth.truth import AssertThat


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.sub_suite("/host/guest/accept_unload")
@allure.title("Positive post request")
def test_host_guest_accept_unload():
    with allure.step("Send request to the server"):
        r = requests.post((T.url() + "/host/guest/accept_unload"), headers=T.headers(),
                          json={"device_id": "AC35EE2644F0"})
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
