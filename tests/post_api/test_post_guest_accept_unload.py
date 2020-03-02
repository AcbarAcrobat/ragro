import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.sub_suite("/guest/accept_unload")
@allure.title("Positive post request")
def test_post_guest_accept_unload():
    with allure.step("Send request to the server"):
        r = requests.post(T.url_() + "/guest/accept_unload", headers=T.headers(),
                          json={"device_id": "15"})
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
