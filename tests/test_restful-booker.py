
import pytest
from playwright.sync_api import Page

def test_get_booking(page: Page):
    response = page.request.get("https://restful-booker.herokuapp.com/booking")

    assert response.status == 200


def test_post_booking(page: Page):

    data = {
        "firstname" : "John",
        "lastname" : "Doe",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01",
    },
    "additionalneeds" : "Breakfast",
    }

    new_booking = page.request.post("https://restful-booker.herokuapp.com/booking", data = data)

    assert new_booking.status == 200
    print(new_booking.json())

    response_body = new_booking.json()
    assert response_body["booking"] ["firstname"] == "John"   
    assert "bookingid" in response_body


def test_update_booking(page: Page):

    data = {
        "firstname" : "Darkus",
        "lastname" : "dark",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01",
    },
    "additionalneeds" : "Breakfast",
    }

    new_booking = page.request.post("https://restful-booker.herokuapp.com/booking", data = data)

    print(new_booking.json())

    booking_id = new_booking.json()["bookingid"]

    updated_data = {
        "firstname" : "Johnny",
        "lastname" : "boy",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01",
    },
    "additionalneeds" : "DInner",
    }

    updated_booking = page.request.put(f"https://restful-booker.herokuapp.com/booking/{booking_id}", data=updated_data, headers = {"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="})
    print(updated_booking.json())
    assert updated_booking.status == 200
    assert updated_booking.json()["firstname"] == "Johnny"

def test_delete(page: Page):

    data = {
        "firstname" : "Master",
        "lastname" : "Ball",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01",
    },
    "additionalneeds" : "Breakfast",
    }
        
    new_booking = page.request.post("https://restful-booker.herokuapp.com/booking", data = data2)

    booking_id = new_booking.json()["bookingid"]

    delete_booking = page.request.delete(f"https://restful-booker.herokuapp.com/booking/{booking_id}", headers = {"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="})

    assert delete_booking.status == 201

    get_delete = page.request.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")

    assert get_delete.status == 404
