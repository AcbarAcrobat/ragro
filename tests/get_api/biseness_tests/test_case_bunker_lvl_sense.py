import json
import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Test case")
@allure.story("Change bunker_level_sens and check response")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_case_bunker_lvl_sense():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="bunker_level_sens", etype="json", evalue=json.dumps({"1": True,
                                                                             "2": False,
                                                                             "3": False,
                                                                             "4": True,
                                                                             "5": False
                                                                             }))
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("bunker_level_sens should have values True, False, False, True, False"):
            AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("sense", {"1": True,
                                                                                             "2": False,
                                                                                             "3": False,
                                                                                             "4": True,
                                                                                             "5": False
                                                                                             })
