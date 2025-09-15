from one_chat.location_sender import LocationSender


def test_send_location_success(requests_mock):
    ls = LocationSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ls.url, json=expected, status_code=200)
    resp = ls.send_location("U1", "B1", "13.7", "100.5", "Bangkok")
    assert resp == expected


def test_send_location_error(requests_mock):
    ls = LocationSender("dummy")
    expected = {"status": "fail", "message": "bad"}
    requests_mock.post(ls.url, json=expected, status_code=400)
    resp = ls.send_location("U1", "B1", "13.7", "100.5", "Bangkok")
    assert resp["status"] == "fail"
