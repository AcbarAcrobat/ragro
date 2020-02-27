import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


TeD = TestData()
LOGGER = logging.getLogger(__name__)


def test_post_guest_accept_unload():
    r = requests.post(TeD.url_() + "/guest/accept_unload", headers=TeD.headers(),
                      json={"device_id": "15"})
    AssertThat(r.status_code).IsEqualTo(200)
    # print(r.json())