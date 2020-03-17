import allure
from truth.truth import AssertThat
import support.test_data2 as TD
from helper.rest import Post
from helper import LOGGER


@allure.parent_suite("POST request")
@allure.sub_suite("/host/guest/accept_unload/remove")
@allure.title("Positive post request")
def test_host_guest_accept_unload_remove():
    with allure.step("Send request to the server"):
        req = Post(TD.url83()).host.guest.accept_unload.remove.body(device_id='15').perf()


    with allure.step("LOGGER get info"):
        LOGGER.info(req.json())
        LOGGER.info(req.status_code)

    with allure.step("Assert status code is 200"):
        AssertThat(req.status_code).IsEqualTo(200)
