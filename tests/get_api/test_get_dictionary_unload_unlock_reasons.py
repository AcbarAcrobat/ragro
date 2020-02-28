import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
from jsonschema import validate
from support.schema.get_dictionary_unload_unlock_reasons import schema
import logging


LOGGER = logging.getLogger(__name__)
T = TestData()


@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_get_dictionary_unload_unlock_reasons():
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url_() + "/get/dictionary/unload_unlock_reasons")
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Validate server response according to our scheme"):
        validate(instance=r.json(), schema=schema)
    with allure.step("Assert Contains Item"):
        AssertThat(r.json()["result"]).ContainsItem("KAGAT", 3)
        AssertThat(r.json()["result"]).ContainsItem("RFID", 1)
        AssertThat(r.json()["result"]).ContainsItem("IDLE_ROTATE", 4)
        AssertThat(r.json()["result"]).ContainsItem("NETWORK", 2)
    LOGGER.info(r.status_code)
    LOGGER.info(r.json())
