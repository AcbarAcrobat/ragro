import time
import allure
import requests
from truth.truth import AssertThat
import tests.mqtt.send_data as mqtt
import support.test_data2 as TD
from helper import LOGGER


@allure.parent_suite("GET request")
@allure.sub_suite("/get/neighbors")
@allure.title("Positive get request")
def test_get_neighbors():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="DEVICE_ID", etype="text", evalue="AC35EE2644F0")
        mqtt.req83(ename="bunker_level", etype="value", evalue="999")
        mqtt.req83(ename="RFID_1", etype="text", evalue="94594156156156")
        time.sleep(2)

    with allure.step("Send request to the server"):
        r = requests.get(TD.url83() + "/get/neighbors")
        r85 = requests.get(TD.url85() + "/get/neighbors")

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)

    with allure.step("LOGGER get info 85"):
        LOGGER.info(r85.json())

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
        
    with allure.step("Assert contains items in json response"):
        AssertThat(r85.json()["result"]).ContainsKey("C010")
        AssertThat(r85.json()["result"]["C010"][0]).ContainsItem("bunker_percentage", 999)
        AssertThat(r85.json()["result"]["C010"][0]["driver"]).ContainsItem("fio", "Школенко Дмитрий Сергеевич")

