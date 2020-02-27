# import requests
# from truth.truth import AssertThat
# from support.testdata import TestData
#
#
# TeD = TestData()


# def test_get_status():
#     r = requests.get(TeD.url_() + "/get/status")
#     AssertThat(r.status_code).IsEqualTo(200)
#     print(r.status_code)
#     validate(instance=r.json(), schema=schema2)
#     print(r.json())


# def test_get_dictionary_vehicle_types():
#     r = requests.get(TeD.url_() + "/get/dictionary/vehicle_types")
#     AssertThat(r.status_code).IsEqualTo(200)
#     print(r.status_code)


# def test_get_dictionary_vehicle_states():
#     r = requests.get(TeD.url_() + "/get/dictionary/vehicle_states")
#     AssertThat(r.status_code).IsEqualTo(200)
#     AssertThat(r.json()["result"]).ContainsItem("HOST_SEARCH_UNLOAD_PERSONALLY", 4)
#     AssertThat(r.json()["result"]).ContainsItem("IDLE_ROTATE", 7)
#     AssertThat(r.json()["result"]).ContainsItem("WAITING_FOR_SECURITY", -3)
#     print(r.json())


# def test_get_dictionary_rfid_states():
#     r = requests.get(TeD.url_() + "/get/dictionary/rfid_states")
#     AssertThat(r.status_code).IsEqualTo(200)
#     AssertThat(r.json()["result"]).ContainsItem("BAD_CARD", 2)
#     AssertThat(r.json()["result"]).ContainsItem("AUTH_OK", 3)
#     AssertThat(r.json()["result"]).ContainsItem("NO_CONNECTION", 0)
#     AssertThat(r.json()["result"]).ContainsItem("REMOVE_CARD", -1)
#     AssertThat(r.json()["result"]).ContainsItem("NO_CARD", 1)
#     print(r.status_code)
#     print(r.json())


# def test_get_dictionary_unload_unlock_reasons():
#     r = requests.get(TeD.url_() + "/get/dictionary/unload_unlock_reasons")
#     AssertThat(r.status_code).IsEqualTo(200)
#     AssertThat(r.json()["result"]).ContainsItem("KAGAT", 3)
#     AssertThat(r.json()["result"]).ContainsItem("RFID", 1)
#     AssertThat(r.json()["result"]).ContainsItem("IDLE_ROTATE", 4)
#     AssertThat(r.json()["result"]).ContainsItem("NETWORK", 2)
#     # print(r.json())


# def test_get_neighbors():
#     r = requests.get(TeD.url_() + "/get/neighbors")
#     AssertThat(r.status_code).IsEqualTo(200)
#     # AssertThat(r.json()["result"]["C020"]).ContainsItem(["bunker_percentage", 0])
#     print(r.json())
#     print(r.status_code)
