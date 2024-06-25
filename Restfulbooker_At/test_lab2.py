import pytest
import requests

import allure

@allure.title("Test Automation")
@allure.description("This test attempts to check the status code.")
@allure.tag("Status Code")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.issue("AUTH-123")
@allure.testcase("Tc-2")

@pytest.mark.smoke
def test_get_single_request():
    response=requests.get("https://restful-booker.herokuapp.com/booking/1?bookingid=1097")
    print(response.text)
    print(response.json())
    print(response.cookies)
    response_status=response.status_code

    assert response_status==200