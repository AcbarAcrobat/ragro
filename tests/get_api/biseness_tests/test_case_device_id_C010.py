import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Test case")
@allure.story("Change DEVICE_ID and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testlink('1-3', '1-3: DEVICE_ID get/status')
def test_case_device_id():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="DEVICE_ID", etype="text", evalue='AC35EE2644F0')  # we wait DEVICE_ID in response
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("DEVICE_ID should be AC35EE2644F0"):
            AssertThat(r.json()["result"]).ContainsItem("device_id", "AC35EE2644F0")
