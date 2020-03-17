import allure
import requests
from truth.truth import AssertThat
from jsonschema import validate
from support.schema.get_dictionary_unload_unlock_reasons import schema
import support.test_data2 as TD
from helper import LOGGER


@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_get_dictionary_unload_unlock_reasons():
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/dictionary/unload_unlock_reasons")

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)

    with allure.step("Validate server response according to our scheme"):
        validate(instance=r.json(), schema=schema)

    with allure.step("Assert Contains Item"):
        AssertThat(r.json()["result"]).ContainsItem("KAGAT", 3)
        AssertThat(r.json()["result"]).ContainsItem("RFID", 1)
        AssertThat(r.json()["result"]).ContainsItem("IDLE_ROTATE", 4)
        AssertThat(r.json()["result"]).ContainsItem("NETWORK", 2)
