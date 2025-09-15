from one_chat import broadcast_message, init, send_message


def test_wrapper_send_message_success(requests_mock):
    # Initialize defaults
    init("dummy", to="U1", bot_id="B1")

    from one_chat.message_sender import MessageSender

    ms = MessageSender("dummy")
    expected = {"status": "success"}
    requests_mock.post(ms.base_url, json=expected, status_code=200)

    resp = send_message(message="hi")
    assert resp == expected


def test_wrapper_broadcast_normalizes_to_string(requests_mock):
    init("dummy", to="U1", bot_id="B1")

    from one_chat.broadcast_sender import BroadcastSender

    bs = BroadcastSender("dummy")
    expected = {"status": "success"}
    req = requests_mock.post(bs.base_url, json=expected, status_code=200)

    resp = broadcast_message(message="hello")
    assert resp == expected
    # Ensure body has list for 'to'
    assert isinstance(req.last_request.json()["to"], list)
    assert req.last_request.json()["to"] == ["U1"]
