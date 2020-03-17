import time
import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import util.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Change unloader_bypass and check state")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_case_no_driver():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="RFID_1", etype="text", evalue="No Card")
        time.sleep(8)
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("State should be -1"):
            AssertThat(r.json()["result"]).ContainsItem("state", -1)

