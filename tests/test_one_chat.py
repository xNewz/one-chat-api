# tests/test_one_chat.py

import pytest
from unittest.mock import patch, MagicMock
from one_chat import init, send_message, broadcast_message, send_location, send_sticker


@pytest.fixture
def setup_one_chat():
    # Initialize OneChat with a mock token
    init("mock_token", "mock_user_id", "mock_bot_id")


@patch('one_chat.message_sender.requests.post')
def test_send_message(mock_post, setup_one_chat):
    # Mock the response of the requests.post
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mock_post.return_value = mock_response

    response = send_message(message="Hello One!")
    assert response == {"status": "success"}
    mock_post.assert_called_once()  # Verify that post was called


@patch('one_chat.broadcast_sender.requests.post')
def test_broadcast_message(mock_post, setup_one_chat):
    # Mock the response of the requests.post
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mock_post.return_value = mock_response

    response = broadcast_message(message="Hello Multi!", to=["mock_user_id", "mock_user_id"])
    assert response == {"status": "success"}
    assert mock_post.call_count == 2  # Verify post was called for each recipient


@patch('one_chat.location_sender.requests.post')
def test_send_location(mock_post, setup_one_chat):
    # Mock the response of the requests.post
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mock_post.return_value = mock_response

    response = send_location(latitude=13.7563, longitude=100.5018, address="Bangkok, Thailand")
    assert response == {"status": "success"}
    mock_post.assert_called_once()


@patch('one_chat.sticker_sender.requests.post')
def test_send_sticker(mock_post, setup_one_chat):
    # Mock the response of the requests.post
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mock_post.return_value = mock_response

    response = send_sticker(sticker_id="mock_sticker_id")
    assert response == {"status": "success"}
    mock_post.assert_called_once()