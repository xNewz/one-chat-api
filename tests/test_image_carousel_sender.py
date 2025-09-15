from one_chat.image_carousel_sender import ImageCarouselSender


def test_send_image_carousel_success(requests_mock):
    ics = ImageCarouselSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ics.base_url, json=expected, status_code=200)
    resp = ics.send_image_carousel("U1", "B1", elements=[{"type": "text", "image": "x"}])
    assert resp == expected


def test_send_image_carousel_error(requests_mock):
    ics = ImageCarouselSender("dummy")
    expected = {"status": "fail", "message": "bad"}
    requests_mock.post(ics.base_url, json=expected, status_code=400)
    resp = ics.send_image_carousel("U1", "B1", elements=[{"type": "text", "image": "x"}])
    assert resp["status"] == "fail"
