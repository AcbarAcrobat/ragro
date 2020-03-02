import logging

import allure
import requests
from truth.truth import AssertThat
from jsonschema import validate
from support.schema.dictionary_vehicle_types_schema import schema
from support.testdata import TestData

T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("GET request")
@allure.sub_suite("/get/dictionary/vehicle_types")
@allure.title("Positive get request")
def test_get_dictionary_vehicle_types():
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url_() + "/get/dictionary/vehicle_types")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert Contsins Items in r.json()[result]"):
        AssertThat(r.json()["result"]).ContainsItem("BEETROOT_HARVESTER", "C030")
        AssertThat(r.json()["result"]).ContainsItem("TRANSPORTER", "C010")
        AssertThat(r.json()["result"]).ContainsItem("REFUELLER", "T090")
        AssertThat(r.json()["result"]).ContainsItem("HARVESTER", "C020")
        AssertThat(r.json()["result"]).ContainsItem("BEETROOT_TRANSPORTER", "C070")
    with allure.step("Validate server response according to our scheme"):
        validate(instance=r.json(), schema=schema)
