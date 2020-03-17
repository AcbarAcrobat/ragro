import allure
import json
import util.mqtt.send_data as mqtt
import pytest
import time


@pytest.fixture(scope='session', autouse=True)
def pikcha():
    yield
    print(r'''           
           \       /
             .---. 
        '-.  |   |  .-'
          ___|   |___
     -=  [           ]  =-
         `---.   .---' 
      __||__ |   | __||__
      '-..-' |   | '-..-'
        ||   |   |   ||
        ||_.-|   |-,_||
      .-"`   `"`'`   `"-.
    .'                   '.''')


@allure.feature("Default condition")
@allure.story("back to Default condition")
@allure.parent_suite("MQTT requests")
@allure.sub_suite("mqtt")
@allure.title("Change all condition")
def default_condition83():
    with allure.step("Send requests to the MQTT83"):
        mqtt.req83(ename="RFID_2", etype="text", evalue="777")
        mqtt.req83(ename="RFID_1", etype="text", evalue="94594156156156")
        mqtt.req83(ename="SIRENA", etype="switch", evalue="0")
        mqtt.req83(ename="BUNKER_SAP_ID", etype="text", evalue="0")
        mqtt.req83(ename="DEVICE_ID", etype="text", evalue="0")
        mqtt.req83(ename="DG400", etype="json", evalue=json.dumps({"net": 0, "units": "KG"}))
        mqtt.req83(ename="LAMP_1", etype="switch", evalue="0")
        mqtt.req83(ename="LAMP_2", etype="switch", evalue="0")
        mqtt.req83(ename="ModBUS_OK", etype="switch", evalue="0")
        mqtt.req83(ename="status_request", etype="switch", evalue="0")
        mqtt.req83(ename="bunker_level", etype="value", evalue="0")
        mqtt.req83(ename="bunker_level_sens", etype="json", evalue=json.dumps({"1": False,
                                                                               "2": False,
                                                                               "3": False,
                                                                               "4": False,
                                                                               "5": False}))
        mqtt.req83(ename="loader_freq", etype="value", evalue="0")
        mqtt.req83(ename="loader_rotate", etype="switch", evalue="0")
        mqtt.req83(ename="unloader_arm", etype="switch", evalue="0")
        mqtt.req83(ename="unloader_bypass", etype="switch", evalue="0")
        mqtt.req83(ename="unloader_freq", etype="value", evalue="0")
        mqtt.req83(ename="unloader_rotate", etype="switch", evalue="0")
        time.sleep(1)
        mqtt.req83(ename="RFID_1", etype="text", evalue="No Card")
        mqtt.req83(ename="RFID_2", etype="text", evalue="No Card")


def default_condition85():
    with allure.step("Send requests to the MQTT85"):
        mqtt.req85(ename="RFID_2", etype="text", evalue="777")
        mqtt.req85(ename="RFID_1", etype="text", evalue="94594156156156")
        mqtt.req85(ename="SIRENA", etype="switch", evalue="0")
        mqtt.req85(ename="BUNKER_SAP_ID", etype="text", evalue="0")
        mqtt.req85(ename="DEVICE_ID", etype="text", evalue="0")
        mqtt.req85(ename="DG400", etype="json", evalue=json.dumps({"net": 0, "units": "KG"}))
        mqtt.req85(ename="LAMP_1", etype="switch", evalue="0")
        mqtt.req85(ename="LAMP_2", etype="switch", evalue="0")
        mqtt.req85(ename="ModBUS_OK", etype="switch", evalue="0")
        mqtt.req85(ename="status_request", etype="switch", evalue="0")
        mqtt.req85(ename="bunker_level", etype="value", evalue="0")
        mqtt.req85(ename="bunker_level_sens", etype="json", evalue=json.dumps({"1": False,
                                                                               "2": False,
                                                                               "3": False,
                                                                               "4": False,
                                                                               "5": False}))
        mqtt.req85(ename="loader_freq", etype="value", evalue="0")
        mqtt.req85(ename="loader_rotate", etype="switch", evalue="0")
        mqtt.req85(ename="unloader_arm", etype="switch", evalue="0")
        mqtt.req85(ename="unloader_bypass", etype="switch", evalue="0")
        mqtt.req85(ename="unloader_freq", etype="value", evalue="0")
        mqtt.req85(ename="unloader_rotate", etype="switch", evalue="0")
        mqtt.req85(ename="RFID_1", etype="text", evalue="No Card")
        mqtt.req85(ename="RFID_2", etype="text", evalue="No Card")


@pytest.fixture(scope="function", autouse=True)
def default_state():
    time.sleep(1)
    yield
    default_condition83()
    time.sleep(1)
