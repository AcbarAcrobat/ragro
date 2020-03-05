import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("GET request")
@allure.sub_suite("/get/neighbors")
@allure.title("Positive get request")
def test_get_neighbors():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644F0")
        mqtt.req(ename="bunker_level", etype="value", evalue="671999")
        mqtt.req(ename="RFID_1", etype="text", evalue="94594156156156")
    with allure.step("Send request to the server"):
        r = requests.get(T.url() + "/get/neighbors")
        r85 = requests.get(T.url85() + "/get/neighbors")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    # with allure.step("LOGGER get info 85"):
    #     LOGGER.info(r85.json())
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    with allure.step("Assert contains items in json response"):
        AssertThat(r85.json()["result"]).ContainsKey("C010")
        AssertThat(r85.json()["result"]["C010"][0]).ContainsItem("bunker_percentage", 671999)
        AssertThat(r85.json()["result"]["C010"][0]["driver"]).ContainsItem("fio", "Школенко Дмитрий Сергеевич")

