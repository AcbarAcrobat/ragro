import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


TeD = TestData()
LOGGER = logging.getLogger(__name__)


def test_host_guest_accept_unload_remove():
    r = requests.post((TeD.url_() + "/host/guest/accept_unload/remove"), headers=TeD.headers(),
                      json={"device_id": "15"})
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())
