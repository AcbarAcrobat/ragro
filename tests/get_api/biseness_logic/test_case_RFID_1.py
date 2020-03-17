import time
import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Test case")
@allure.story("Change RFID_1 and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-7', '1-7:200 RFID_1 get/status')
def test_case_RFID_1():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="RFID_1", etype="text", evalue="94594156156156")
        # we wait DEVICE_ID in response
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("RFID_1 should have fio Школенко Дмитрий Сергеевич"):
            AssertThat(r.json()["result"]["driver"]).ContainsItem("fio", "Школенко Дмитрий Сергеевич")
