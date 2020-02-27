import requests
from truth.truth import AssertThat
from support.testdata import TestData
import logging


T = TestData()
LOGGER = logging.getLogger(__name__)


def test_host_guest_accept_unload():
    r = requests.post((T.url_() + "/host/guest/accept_unload"), headers=T.headers())
    pass
