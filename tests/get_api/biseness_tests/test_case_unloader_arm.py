import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt
import tests.get_api.biseness_tests.test_case_device_id_C010 as tdi


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Test case")
@allure.story("Change DG400 and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_case_unloader_arm():
    with allure.step("Send requests to the MQTT"):
        tdi.test_case_device_id()
        mqtt.req(ename="RFID_1", etype="text", evalue="94594156156156")
        mqtt.req(ename="unloader_arm", etype="switch", evalue="1")
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("reaper should have rotate True"):
            AssertThat(r.json()["result"]["mechanization"]["worm"]).ContainsItem("lock", False)
            with allure.step("Check state 0"):
                AssertThat(r.json()["result"]).ContainsItem("state", 0)
    # with allure.step("Change reaper condition to default"):
    #     mqtt.req(ename="loader_rotate", etype="switch", evalue="0")
