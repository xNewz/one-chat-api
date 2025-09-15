from one_chat.sticker_sender import StickerSender


def test_send_sticker_success(requests_mock):
    ss = StickerSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ss.api_url, json=expected, status_code=200)
    resp = ss.send_sticker("U1", "B1", "STK1")
    assert resp == expected


def test_send_sticker_error(requests_mock):
    ss = StickerSender("dummy")
    expected = {"status": "fail", "message": "Error"}
    requests_mock.post(ss.api_url, json=expected, status_code=400)
    resp = ss.send_sticker("U1", "B1", "STK1")
    assert resp["status"] == "fail"
