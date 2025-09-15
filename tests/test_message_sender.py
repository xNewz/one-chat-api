from one_chat.message_sender import MessageSender


def test_send_message_success(requests_mock):
    ms = MessageSender("dummy")
    expected = {"status": "success", "message": "ok"}
    requests_mock.post(ms.base_url, json=expected, status_code=200)

    resp = ms.send_message("U1", "B1", "hello")
    assert resp == expected


def test_send_message_error(requests_mock):
    ms = MessageSender("dummy")
    expected = {"status": "fail", "message": "bad request"}
    requests_mock.post(ms.base_url, json=expected, status_code=400)

    resp = ms.send_message("U1", "B1", "hello")
    assert resp["status"] == "fail"
    assert "message" in resp


def test_send_template_success(requests_mock):
    ms = MessageSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ms.base_url, json=expected, status_code=200)
    resp = ms.send_template("U1", "B1", template=[{"title": "t"}])
    assert resp == expected


def test_send_file_success(tmp_path, requests_mock):
    ms = MessageSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ms.base_url, json=expected, status_code=200)
    f = tmp_path / "x.txt"
    f.write_text("hi")
    resp = ms.send_file("U1", "B1", str(f))
    assert resp == expected


def test_send_webview_requires_protocol():
    ms = MessageSender("dummy")
    resp = ms.send_webview("U1", "B1", url="google.com")
    assert resp["status"] == "fail"
    assert "protocol" in resp["message"].lower()


def test_send_webview_success(requests_mock):
    ms = MessageSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ms.base_url, json=expected, status_code=200)
    resp = ms.send_webview("U1", "B1", url="https://example.com")
    assert resp == expected
