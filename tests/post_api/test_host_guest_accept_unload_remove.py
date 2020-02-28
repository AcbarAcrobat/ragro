import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


TeD = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST requests")
@allure.sub_suite("/host/guest/accept_unload/remove")
@allure.title("POSITIVE tests")
def test_host_guest_accept_unload_remove():
    with allure.step("Send request to the server"):
        r = requests.post((TeD.url_() + "/host/guest/accept_unload/remove"), headers=TeD.headers(),
                          json={"device_id": "15"})
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    LOGGER.info(r.json())
    LOGGER.info(r.status_code)
