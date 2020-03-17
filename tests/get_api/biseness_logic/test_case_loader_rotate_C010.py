import time
import json
import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt
import tests.get_api.biseness_logic.test_case_RFID_1 as tc
import tests.get_api.biseness_logic.test_case_device_id_C010 as tdi



T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Test case")
@allure.story("Change loader_rotate and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-13', '1-13: loader_rotate get/status')
def test_case_loader_rotate():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="DEVICE_ID", etype="text", evalue='AC35EE2644DA')
        mqtt.req(ename="loader_rotate", etype="switch", evalue="1")
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("reaper should have rotate True"):
            AssertThat(r.json()["result"]["mechanization"]["reaper"]).ContainsItem("rotate", True)
