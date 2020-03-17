import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import tests.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Change RFID_2 and check response")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-8', '1-8: RFID_2 get/status')
def test_case_RFID_2():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="RFID_2", etype="text", evalue="99296465799940")
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("RFID_2 should have name САМОСВАЛ КАМАЗ 55102"):
            AssertThat(r.json()["result"]["guest"]).ContainsItem("name", "САМОСВАЛ КАМАЗ 55102")
            AssertThat(r.json()["result"]["guest"]).ContainsItem("card_uid", "99296465799940")
