from one_chat.get_friends_and_groups import FriendAndGroupManager


def test_fetch_friends_and_groups_success(requests_mock):
    fm = FriendAndGroupManager("dummy")
    expected = {
        "status": "success",
        "list_friend": [{"one_id": "U1"}],
        "list_group": [{"group_id": "G1"}],
    }
    requests_mock.post(fm.base_url, json=expected, status_code=200)
    resp = fm.fetch_friends_and_groups("B1")
    assert resp == expected


def test_list_methods_parse_success(requests_mock):
    fm = FriendAndGroupManager("dummy")
    payload = {
        "status": "success",
        "list_friend": [{"one_id": "U1"}, {"one_id": "U2"}],
        "list_group": [{"group_id": "G1"}, {"group_id": "G2"}],
    }
    requests_mock.post(fm.base_url, json=payload, status_code=200)
    assert fm.list_all_friends("B1") == payload["list_friend"]
    assert fm.list_friend_ids("B1") == ["U1", "U2"]
    assert fm.list_all_groups("B1") == payload["list_group"]
    assert fm.list_group_ids("B1") == ["G1", "G2"]


def test_fetch_error_handling(requests_mock):
    fm = FriendAndGroupManager("dummy")
    error = {"status": "fail", "message": "bad"}
    requests_mock.post(fm.base_url, json=error, status_code=400)
    resp = fm.fetch_friends_and_groups("B1")
    assert resp["status"] == "fail"
