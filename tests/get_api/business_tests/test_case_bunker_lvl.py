import requests
import allure
from truth.truth import AssertThat
import tests.mqtt.send_data as mqtt
import support.test_data2 as TD
from helper import LOGGER
from helper.rest import Get


@allure.feature("Test case")
@allure.story("Change bunker_level and check response")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-9', '1-9: bunker_level get/status')
def test_case_bunker_lvl():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="bunker_level", etype="value", evalue="81")

    with allure.step("Send GET request to the server"):
        # r = requests.get(TD.url83() + "/get/status")
        r = Get(TD.url83()).get.status.perf()

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
        
    with allure.step("Assert Contains Item"):
        with allure.step("bunker_level should have value 999"):
            AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("percentage", 81)
