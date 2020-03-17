import allure
import requests
from truth.truth import AssertThat
from jsonschema import validate
from support.schema.dictionary_vehicle_states_schema import schema
import support.test_data2 as TD
from helper import LOGGER


@allure.story("Test case for validate json in response")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/dictionary/vehicle_states")
@allure.title("Positive get request")
def test_get_dictionary_vehicle_states():
    with allure.step("Send request to the server"):
        r = requests.get(TD.url83() + "/get/dictionary/vehicle_states")

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)

    with allure.step("Validate server response according to our scheme"):
        validate(instance=r.json(), schema=schema)

    with allure.step("Assert Contains Items in r.json()['result']"):
        AssertThat(r.json()["result"]).ContainsItem("HOST_SEARCH_UNLOAD_PERSONALLY", 4)
        AssertThat(r.json()["result"]).ContainsItem("IDLE_ROTATE", 7)
        AssertThat(r.json()["result"]).ContainsItem("WAITING_FOR_SECURITY", -3)
        AssertThat(r.json()["result"]).ContainsItem("NO_IGNITION", -2)
        AssertThat(r.json()["result"]).ContainsItem("GUEST_START_UNLOAD", 6)
        AssertThat(r.json()["result"]).ContainsItem("HOST_ACCEPT_UNLOAD", 1)
        AssertThat(r.json()["result"]).ContainsItem("HOST_SEARCH_UNLOAD_PERSONALLY", 4)
        AssertThat(r.json()["result"]).ContainsItem("WAITING_FOR_INIT_END", -4)
        AssertThat(r.json()["result"]).ContainsItem("DEFAULT", 0)
        AssertThat(r.json()["result"]).ContainsItem("NO_DRIVER", -1)
        AssertThat(r.json()["result"]).ContainsItem("GUEST_ACCEPT_UNLOAD", 5)
        AssertThat(r.json()["result"]).ContainsItem("HOST_SEARCH_UNLOAD", 3)
        AssertThat(r.json()["result"]).ContainsItem("TURN_OFF", -5)

