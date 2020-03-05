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


@allure.feature("Test case check biseness logic")
@allure.story("Send to mqtt variable and wait response")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_get_status():
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    # with allure.step("Validate server response according to our scheme"):
    #     validate(instance=r.json(), schema=schema)
