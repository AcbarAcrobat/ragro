import json
import requests
import allure
from truth.truth import AssertThat
from support.testdata import TestData
from jsonschema import validate
from support.schema.get_status_schema import schema
import logging
import tests.mqtt.example as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("GET request")
@allure.sub_suite("/get/status")
@allure.title("Positive get request")
def test_get_status():
    with allure.step("Send requests for MQTT"):
        mqtt.req(ename="bunker_level", etype="value", evalue="12589")
        mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
        mqtt.req(ename="DG400", etype="json", evalue=json.dumps({"net": 777, "units": "KG"}))
        mqtt.req(ename="bunker_level_sens", etype="json", evalue=json.dumps({"1": False,
                                                                             "2": False,
                                                                             "3": True,
                                                                             "4": True,
                                                                             "5": False}))
        mqtt.req(ename="ignition", etype="switch", evalue="1")
        # mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
        # mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
        # mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
        # mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
        # mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
        # mqtt.req(ename="DEVICE_ID", etype="text", evalue="AC35EE2644DA")
    with allure.step("Send GET request to the server"):
        r = requests.get(T.url() + "/get/status")
    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)
    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
    # with allure.step("Validate server response according to our scheme"):
    #     validate(instance=r.json(), schema=schema)
    with allure.step("Assert Contains Item"):
        AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("percentage", 12589)
        AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("weight", 777)
        AssertThat(r.json()["result"]["mechanization"]["bunker"]).ContainsItem("sense", {'1': False,
                                                                                         '2': False,
                                                                                         '3': True,
                                                                                         '4': True,
                                                                                         '5': False})
        AssertThat(r.json()["result"]).ContainsItem("device_id", "AC35EE2644DA")
    #     AssertThat(r.json()["result"]).ContainsItem("device_id", "AC35EE2644A7")
    #     AssertThat(r.json()["result"]["mechanization"]["worm"]).ContainsItem("rotate", False)
