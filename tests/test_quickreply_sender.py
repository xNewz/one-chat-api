from one_chat.quickreply_sender import QuickReplySender


def test_send_quickreply_success(requests_mock):
    qs = QuickReplySender("dummy")
    expected = {"status": "success"}
    requests_mock.post(qs.base_url, json=expected, status_code=200)
    resp = qs.send_quickreply("U1", "B1", "hi", quick_reply=[{"label": "A", "type": "text"}])
    assert resp == expected


def test_send_quickreply_error(requests_mock):
    qs = QuickReplySender("dummy")
    expected = {"status": "fail", "message": "bad"}
    requests_mock.post(qs.base_url, json=expected, status_code=400)
    resp = qs.send_quickreply("U1", "B1", "hi", quick_reply=[{"label": "A", "type": "text"}])
    assert resp["status"] == "fail"
