import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
from support.schema.dictionary_rdind_states_schema import schema
from jsonschema import validate
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("GET request")
@allure.sub_suite("/get/dictionary/rfid_states")
@allure.title("Positive get request")
def test_get_dictionary_rfid_states():
    with allure.step("Send request to the server"):
        r = requests.get(T.url_() + "/get/dictionary/rfid_states")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Validate server response according to our scheme"):
        validate(instance=r.json(), schema=schema)
    with allure.step("Assert Contains Items"):
        AssertThat(r.json()["result"]).ContainsItem("BAD_CARD", 2)
        AssertThat(r.json()["result"]).ContainsItem("AUTH_OK", 3)
        AssertThat(r.json()["result"]).ContainsItem("NO_CONNECTION", 0)
        AssertThat(r.json()["result"]).ContainsItem("REMOVE_CARD", -1)
        AssertThat(r.json()["result"]).ContainsItem("NO_CARD", 1)