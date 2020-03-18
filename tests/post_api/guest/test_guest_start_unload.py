import allure
import requests
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
from helper.rest import Post, Get
import util.mqtt.send_data as mqtt


@allure.parent_suite("POST request")
@allure.suite('Guest')
@allure.sub_suite("/guest/start_unload")
@allure.title("Начало выгрузки по буеспроводной идентификации (разблокирует шнек)")
def test_guest_start_unload():
    device_id_1 = "AC35EE2644F0"
    device_id_2 = "AC35EE26450B"

    url = TD.url85() + '/guest/start_unload'
    body = { "device_id": device_id_1 }

    mqtt.req83(ename="DEVICE_ID", etype="text", evalue=device_id_1)
    mqtt.req83(ename="RFID_1", etype="text", evalue="94594156156156")
    mqtt.req83(ename="RFID_2", etype="text", evalue="777")
    mqtt.req83(ename="bunker_level", etype="value", evalue="81")
    
    mqtt.req85(ename="DEVICE_ID", etype="text", evalue=device_id_2)
    mqtt.req85(ename="RFID_1", etype="text", evalue="94594156150000")
    mqtt.req85(ename="RFID_2", etype="text", evalue="777")
    mqtt.req85(ename="bunker_level", etype="value", evalue="0")


    req = Post(TD.url83()).host.search.start_unload.perf()
    LOGGER.debug(r'\n*** host.search.start_unload :: ' + str(req.json()))


    mqtt.req83(ename="unloader_bypass", etype="switch", evalue="1")
    req = Get(TD.url83()).get.status.perf()
    LOGGER.debug(r'\n*** get.status ::' + str(req.json())) # state=-3, bypass=True


    req = Post(TD.url83()).host.start_unload.body(
        device_id=device_id_1,
        rfid='94594156156156',
        reason=1
    ).perf()
    LOGGER.debug(r'\n*** host.start_unload ::' + str(req.json()))
