import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import tests.mqtt.send_data as mqtt


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
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("reaper should have rotate True"):
            AssertThat(r.json()["result"]["mechanization"]["reaper"]).ContainsItem("rotate", True)
