import allure
import requests
from truth.truth import AssertThat
import support.test_data2 as TD
from helper import LOGGER


@allure.parent_suite("POST request")
@allure.sub_suite("/host/start_unload")
@allure.title("Positive post request")
def test_host_start_unload():
    with allure.step("Send request to the server"):
        r = requests.post(
            TD.url83() + "/host/start_unload",
            headers=TD.headers(),
            json={
                "device_id": "AC35EE2644F0",
                "rfid": "94594156156156",
                "reason": 1
            })

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
