import json
import requests
import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import util.mqtt.send_data as mqtt


@allure.feature("Test case")
@allure.story("Send GPSD_TPV and check")
@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
@allure.testcase('1-5', '1-5: GPSD_TPV get/status')
def test_send_gpsd_tpv():
    with allure.step("Send requests to the MQTT"):
        mqtt.req83(ename="GPSD_TPV", etype="json",
                   evalue=json.dumps({"class": "TPV", "time": "2020-03-31T04:50:20.10Z", "ept": 0.005,
                                      "lat": 46.498204497, "lon": 7.568061439, "alt": 1327.689,
                                      "epx": 15.319, "epy": 17.054, "epv": 124.484, "track": 10.3797,
                                      "speed": 0.091, "climb": -0.085, "eps": 34.11, "mode": 3}))
    with allure.step("Send GET request to the server"):
        r = requests.get(TD.url83() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert Contains Item"):
        with allure.step("GPSD_TPV should be True"):
            AssertThat(r.json()["result"]["availability"]).ContainsItem("GPS", True)
