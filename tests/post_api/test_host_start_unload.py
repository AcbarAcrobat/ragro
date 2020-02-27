import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


def test_host_start_unload():
    r = requests.post(T.url_() + "/host/start_unload", headers=T.headers(),
                      json={
                              "device_id": "11",
                              "rfid": "12345",
                              "reason": 1
                      })
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
