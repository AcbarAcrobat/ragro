import allure
from truth.truth import AssertThat
import util.mqtt.send_data as mqtt
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
        # mqtt.req83(ename="DEVICE_ID", etype="text", evalue='AC35EE2644DA')
        mqtt.req83(ename="bunker_level", etype="value", evalue="81")

    with allure.step("Send GET request to the server"):
        # req = requests.get(TD.url83() + "/get/status")
        req = Get(TD.url83()).get.status.perf()

    with allure.step("LOGGER get info"):
        LOGGER.info(req.json())
        LOGGER.info(req.status_code)
        
    with allure.step("Assert Contains Item"):
        with allure.step("bunker_level should have value 81"):
            AssertThat(req.json()["result"]["mechanization"]["bunker"]).ContainsItem("percentage", 81)
