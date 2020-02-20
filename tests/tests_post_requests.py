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


def test_guest_start_unload():
    pass


def test_host_search_start_unload():
    r = requests.post(TeD.url_() + "/host/search/start_unload", headers=TeD.headers())
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())


def test_search_start_unload_remove():
    r = requests.post(TeD.url_() + "/host/search/start_unload/remove", headers=TeD.headers())
    AssertThat(r.status_code).IsEqualTo(200)
    LOGGER.info(r )



def test_host_guest_accept_unload():
    r = requests.post((TeD.url_() + "/host/guest/accept_unload"), headers=TeD.headers())
    pass


def test_host_guest_accept_unload_remove():
    r = requests.post((TeD.url_() + "/host/guest/accept_unload/remove"), headers=TeD.headers(),
                      json={"device_id": "15"})
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())


def test_host_start_unload():
    r = requests.post(TeD.url_() + "/host/start_unload", headers=TeD.headers(),
                      json={
                              "device_id": "11",
                              "rfid": "12345",
                              "reason": 1
                      })
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())


def test_host_start_unload_remove():
    r = requests.post(TeD.url_() + "/host/start_unload/remove", headers=TeD.headers())
    AssertThat(r.status_code).IsEqualTo(200)
    print(r.json())


def test_host_free():
    r = requests.post(TeD.url_() + "/host/free", headers=TeD.headers())
    AssertThat(r.status_code).IsEqualTo(200)
    LOGGER.info(r.json())










