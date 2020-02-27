import allure
import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


def test_host_free():
    r = requests.post(T.url_() + "/host/free", headers=T.headers())
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
