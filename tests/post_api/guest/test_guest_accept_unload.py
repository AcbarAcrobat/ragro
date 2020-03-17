import allure
from truth.truth import AssertThat
from support import test_data2 as TD
from helper.rest import Post, Get
from helper import LOGGER
import tests.mqtt.send_data as mqtt


@allure.parent_suite("POST request")
@allure.suite('Guest')
@allure.sub_suite("/guest/accept_unload")
@allure.title("Принятия запроса на разгрузку по беспроводной идентификации")
def test_guest_accept_unload():
    device_id = "AC35EE26450B"

    mqtt.req(ename="DEVICE_ID", etype="text", evalue=device_id)
    mqtt.req(ename="RFID_1", etype="text", evalue="94594156156156")
    mqtt.req(ename="RFID_2", etype="text", evalue="777")
    mqtt.req(ename="bunker_level", etype="value", evalue="81")


    req = Post(TD.url83()).host.search.start_unload.perf()
    LOGGER.debug(r'\n*** host.search.start_unload :: ' + str(req.json()))


    mqtt.req(ename="unloader_bypass", etype="switch", evalue="1")
    req = Get(TD.url83()).get.status.perf()
    LOGGER.debug(r'\n*** get.status ::' + str(req.json())) # state=-3, bypass=True


    req = Post(TD.url85()).guest.accept_unload.body(device_id=device_id).perf()
    mqtt.req85(ename="RFID_2", etype="text", evalue="777")
    LOGGER.debug(r'\n*** guest.accept_unload ::' + str(req.json()))
