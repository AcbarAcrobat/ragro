import time
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
@allure.story("Change DG400 and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_case_dg400():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="DG400", etype="json", evalue=json.dumps({"net": 0.8, "units": "KG"}))
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("DG400 should have net 7891"):
            AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("weight", 0.8)
