import allure
import json
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt

T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.feature("Default condition")
@allure.story("back to Default condition")
@allure.parent_suite("MQTT requests")
@allure.sub_suite("mqtt")
@allure.title("Change all condition")
def mqtt_condition():
    with allure.step("Send requests to the MQTT"):
        mqtt.req(ename="BUNKER_SAP_ID", etype="text", evalue="0")
        mqtt.req(ename="DEVICE_ID", etype="text", evalue="0")
        mqtt.req(ename="DG400", etype="json", evalue=json.dumps({"net": 0, "units": "KG"}))
        # mqtt.req(ename="GPSD_TPV", etype="json", evalue="0")
        mqtt.req(ename="LAMP_1", etype="switch", evalue="0")
        mqtt.req(ename="LAMP_2", etype="switch", evalue="0")
        mqtt.req(ename="ModBUS_OK", etype="switch", evalue="0")
        mqtt.req(ename="RFID_1", etype="text", evalue="0")
        mqtt.req(ename="RFID_2", etype="text", evalue="0")
        mqtt.req(ename="SIRENA", etype="switch", evalue="0")
        mqtt.req(ename="status_request", etype="switch", evalue="0")
        mqtt.req(ename="bunker_level", etype="value", evalue="0")
        mqtt.req(ename="bunker_level_sens", etype="json", evalue=json.dumps({"1": False,
                                                                             "2": False,
                                                                             "3": False,
                                                                             "4": False,
                                                                             "5": False}))
        mqtt.req(ename="loader_freq", etype="value", evalue="0")
        mqtt.req(ename="loader_rotate", etype="switch", evalue="0")
        mqtt.req(ename="unloader_arm", etype="switch", evalue="0")
        mqtt.req(ename="unloader_bypass", etype="switch", evalue="0")
        mqtt.req(ename="unloader_freq", etype="value", evalue="0")
        mqtt.req(ename="unloader_rotate", etype="switch", evalue="0")


