import json
import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
from helper.rest import Get
import tests.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Change bunker_level_sens and check response")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-10', '1-10: bunker_level_sens get/status')
def test_case_bunker_lvl_sense():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="bunker_level_sens", etype="json", evalue=json.dumps({"1": True,
                                                                             "2": False,
                                                                             "3": False,
                                                                             "4": True,
                                                                             "5": False
                                                                               }))
    with allure.step("Send GET request to the server"):
        # r = requests.get(TD.url83() + "/get/status")
        req = Get(TD.url83().get.status.perf())
    with allure.step("LOGGER get info"):
        LOGGER.info(req.json())
        LOGGER.info(req.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("bunker_level_sens should have values True, False, False, True, False"):
            AssertThat(req.json()["result"]["mechanization"]["bunker"]).ContainsItem("sense", {"1": True,
                                                                                             "2": False,
                                                                                             "3": False,
                                                                                             "4": True,
                                                                                             "5": False
                                                                                             })
