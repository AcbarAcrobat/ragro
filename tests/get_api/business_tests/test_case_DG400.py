import json
import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import tests.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Change DG400 and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-4', '1-4: DG400 get/status')
def test_case_dg400():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="DG400", etype="json", evalue=json.dumps({"net": 0.8, "units": "KG"}))
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("DG400 should have net 7891"):
            AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("weight", 0.8)
