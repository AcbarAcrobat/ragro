import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)



@allure.parent_suite("GET request")
@allure.sub_suite("/get/neighbors")
@allure.title("Positive get request")
def test_get_neighbors():
    with allure.step("Send request to the server"):
        r = requests.get(T.url_() + "/get/neighbors")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert contains items in json response"):
        AssertThat(r.json()["result"]["C020"][0]).ContainsAnyIn(["bunker_percentage", 0])
        AssertThat(r.json()["result"]["C020"][0]).ContainsAnyIn(["reg_num", "7997ЕЕ31"])
