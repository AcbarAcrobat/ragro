import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


TeD = TestData()
LOGGER = logging.getLogger(__name__)


def test_host_start_unload_remove():
    r = requests.post(TeD.url_() + "/host/start_unload/remove", headers=TeD.headers())
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
