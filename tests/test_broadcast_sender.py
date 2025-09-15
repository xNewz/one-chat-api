from one_chat.broadcast_sender import BroadcastSender


def test_broadcast_validates_list_type():
    bs = BroadcastSender("dummy")
    resp = bs.broadcast_message("B1", "not-a-list", "hi")  # type: ignore[arg-type]
    assert resp["status"] == "fail"


def test_broadcast_limits_recipients():
    bs = BroadcastSender("dummy")
    too_many = [f"U{i}" for i in range(101)]
    resp = bs.broadcast_message("B1", too_many, "hi")
    assert resp["status"] == "fail"
    assert "out of range" in resp["message"]
