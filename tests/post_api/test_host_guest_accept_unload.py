import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


@allure.parent_suite("POST request")
@allure.sub_suite("/host/guest/accept_unload")
@allure.title("Positive post request")
def test_host_guest_accept_unload():
    r = requests.post((T.url_() + "/host/guest/accept_unload"), headers=T.headers())
    pass
