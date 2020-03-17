import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging
import tests.mqtt.send_data as mqtt


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.suite('Guest')
@allure.sub_suite("/guest/accept_unload")
@allure.title("Начало выгрузки по буеспроводной идентификации (разблокирует шнек)")
def test_guest_start_unload():
    device_id = "AC35EE26450B"
    url = T.url85() + '/guest/start_unload'
    body = { "device_id": device_id }

    mqtt.req(ename="DEVICE_ID", etype="text", evalue=device_id)

    with allure.step("Начало выгрузки"):
        r = requests.post(url, json=body, headers=T.headers())

    LOGGER.debug(r.json())
    LOGGER.debug(r.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)

    with allure.step('Validate schema'):
        pass
