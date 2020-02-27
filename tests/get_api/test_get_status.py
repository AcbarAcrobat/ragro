import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
from jsonschema import validate
from support.schema.get_status_schema import schema

T = TestData()


@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_get_status():
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url_() + "/get/status")
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert Contains Item"):
        AssertThat(r.json()["result"]).ContainsItem("RFID_guest_state", 0)
        AssertThat(r.json()["result"]).ContainsItem("RFID_guest_unload_request", False)
        AssertThat(r.json()["result"]).ContainsItem("RFID_driver_state", 3)
        AssertThat(r.json()["result"]).ContainsItem("device_id", "AC35EE2644A7")
        AssertThat(r.json()["result"]["mechanization"]["worm"]).ContainsItem("rotate", False)
    with allure.step("Validate server response according to our scheme"):
        validate(instance=r.json(), schema=schema)
    print(r.status_code)
    # print(r.json())
