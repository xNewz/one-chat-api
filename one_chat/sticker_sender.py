# one_chat/sticker_sender.py

from typing import Optional

import requests

DEFAULT_TIMEOUT = (5, 15)


class StickerSender:
    """Send stickers via the message API."""

    def __init__(self, authorization_token: str):
        """Initialize with Bearer token (with/without prefix)."""
        if authorization_token.startswith("Bearer "):
            authorization_token = authorization_token.replace("Bearer ", "", 1)
        self.authorization_token = authorization_token
        self.api_url = "https://chat-api.one.th/message/api/v1/push_message"

    def send_sticker(
        self,
        to: str,
        bot_id: str,
        sticker_id: Optional[str],
        custom_notification: Optional[str] = None,
    ) -> dict:
        """Send a sticker by `sticker_id` to the recipient `to`."""
        headers = {
            "Authorization": f"Bearer {self.authorization_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "to": to,
            "bot_id": bot_id,
            "type": "sticker",
            "sticker_id": sticker_id,
        }
        if custom_notification:
            payload["custom_notification"] = custom_notification

        try:
            response = requests.post(
                self.api_url, headers=headers, json=payload, timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 200:
                return response.json()
            else:
                return self._handle_error(response)
        except requests.exceptions.RequestException as e:
            return {"status": "fail", "message": f"Request failed: {str(e)}"}

    def _handle_error(self, response: requests.Response) -> dict:
        """Normalize API error responses for consistency."""
        try:
            error_response = response.json()
            return {
                "status": error_response.get("status", "fail"),
                "message": error_response.get("message", "Unknown error occurred."),
            }
        except ValueError:
            return {"status": "fail", "message": "Invalid response from the server."}
