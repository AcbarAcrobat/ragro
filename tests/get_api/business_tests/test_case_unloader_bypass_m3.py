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
@allure.testcase('1-15', '1-15: unloader_bypass get/status')
def test_case_unloader_by_pass():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="RFID_1", etype="text", evalue="94594156156156")
        mqtt.req83(ename="unloader_bypass", etype="switch", evalue="1")  # we wait state -3 in response

    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
        
    with allure.step("Assert Contains Item"):
        with allure.step("State should be -3"):
            AssertThat(r.json()["result"]).ContainsItem("state", -3)
            AssertThat(r.json()["result"]["mechanization"]["worm"]).ContainsItem("bypass", True)
