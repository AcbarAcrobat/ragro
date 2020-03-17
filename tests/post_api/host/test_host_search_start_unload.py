import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
from support import test_data2 as TD
from support import LOGGER
import tests.get_api.biseness_tests.test_case_bunker_lvl as bunker


@allure.parent_suite("POST request")
@allure.sub_suite("/host/search/start_unload")
@allure.title("Positive post request")
def test_host_search_start_unload():
    with allure.step("Send request to the server"):
        bunker.test_case_bunker_lvl()
        r = requests.post(TD.url() + "/host/search/start_unload", headers=TD.headers())

    with allure.step("LOGGER get info"):
        LOGGER.info(r.json())
        LOGGER.info(r.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(r.status_code).IsEqualTo(200)
