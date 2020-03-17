import allure
import requests
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER
import tests.mqtt.send_data as mqtt


@allure.parent_suite("POST request")
@allure.suite('Guest')
@allure.sub_suite("/guest/accept_unload")
@allure.title("Начало выгрузки по буеспроводной идентификации (разблокирует шнек)")
def test_guest_start_unload():
    device_id = "AC35EE26450B"
    url = TD.url85() + '/guest/start_unload'
    body = { "device_id": device_id }

    mqtt.req83(ename="DEVICE_ID", etype="text", evalue=device_id)

    with allure.step("Начало выгрузки"):
        r = requests.post(TD.url85().guest.start.unload.perf(), json=body, headers=TD.headers())

    LOGGER.debug(r.json())
    LOGGER.debug(r.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)

    with allure.step('Validate schema'):
        pass
