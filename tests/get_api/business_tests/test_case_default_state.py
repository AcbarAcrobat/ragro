import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import tests.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Change rfid and check state")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_case_default_state():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="unloader_bypass", etype="switch", evalue="1")
        mqtt.req83(ename="RFID_1", etype="text", evalue="777")  # we wait state 0 in response
        mqtt.req83(ename="RFID_1", etype="text", evalue="94594156156156")
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("State should be -0"):
            AssertThat(r.json()["result"]).ContainsItem("state", 0)
