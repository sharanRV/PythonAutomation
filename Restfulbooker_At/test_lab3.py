import pytest  #pip install pytest
import requests  #pip install requests
import allure  #pip install allure


@allure.description("Tc#1 Verify the Create Booking")
@allure.title("Create Booking Crud")
@pytest.mark.crud
def test_create_booking_positive():
    #URL
    #Headers
    #Payload/Data/Body
    # Request
    #Auth(No Auth In Post)
    # Method
    #response
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL=base_url+base_path
    headers = {"Content-Type": "application/json"}
    payload={
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    response=requests.post(url=URL,headers=headers,json=payload)
    #Response Body Verification
    #Headers
    #Status Code
    #JSON Schema Validation
    #Time Response

    assert response.status_code==200
    print(response.headers)
    response_json=response.json()
    booking_id=response_json["bookingid"]
    assert booking_id is not None
    assert booking_id >0
    assert type(booking_id)==int
    firstname=response_json["booking"]["firstname"]
    assert firstname=="Jim"
    checkin_date=response_json["booking"]["bookingdates"]["checkin"]
    assert checkin_date=="2018-01-01"


@allure.description("Tc#2 Verify the Booking is not created with data")
@allure.title("Create Booking is not with data")
@pytest.mark.crud
def test_create_booking_negative():
    #URL
    #Headers
    #Payload/Data/Body
    # Request
    #Auth(No Auth In Post)
    # Method
    #response
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL=base_url+base_path
    headers = {"Content-Type": "application/json"}
    payload={ }

    response=requests.post(url=URL,headers=headers,json=payload)
    print(type(URL))
    print(type(headers))
    #Response Body Verification
    #Headers
    #Status Code
    #JSON Schema Validation
    #Time Response

    #Assertion
    assert response.status_code==500


