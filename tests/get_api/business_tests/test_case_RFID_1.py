import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import util.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Change RFID_1 and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-7', '1-7:200 RFID_1 get/status')
def test_case_RFID_1():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="RFID_1", etype="text", evalue="94594156156156")
        # we wait DEVICE_ID in response
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("RFID_1 should have fio Школенко Дмитрий Сергеевич"):
            AssertThat(r.json()["result"]["driver"]).ContainsItem("fio", "Школенко Дмитрий Сергеевич")
