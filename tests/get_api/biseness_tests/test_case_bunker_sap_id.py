import time
import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Test case")
@allure.story("Change BUNKER_SAP_ID and check sap_id")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_case_bunker_sap_id():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="BUNKER_SAP_ID", etype="text", evalue='🇺🇸🇷🇺🇸 🇦🇫🇦🇲🇸')
        # we wait sap_id in response
        time.sleep(1)
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("sap_id should be 🇺🇸🇷🇺🇸 🇦🇫🇦🇲🇸"):
            AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("sap_id", "🇺🇸🇷🇺🇸 🇦🇫🇦🇲🇸")
