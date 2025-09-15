from typing import Optional

import requests

DEFAULT_TIMEOUT = (5, 15)


class LocationSender:
    def __init__(self, authorization_token: str):
        if authorization_token.startswith("Bearer "):
            authorization_token = authorization_token.replace("Bearer ", "", 1)
        self.authorization_token = authorization_token
        self.url = "https://chat-api.one.th/message/api/v1/push_message"

    def send_location(
        self,
        to: str,
        bot_id: str,
        latitude: Optional[str],
        longitude: Optional[str],
        address: Optional[str],
        custom_notification: Optional[str] = None,
    ) -> dict:
        headers = {
            "Authorization": f"Bearer {self.authorization_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "to": to,
            "bot_id": bot_id,
            "type": "location",
            "latitude": latitude,
            "longitude": longitude,
            "address": address,
            "custom_notification": custom_notification,
        }

        try:
            response = requests.post(
                self.url, headers=headers, json=payload, timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 200:
                return response.json()
            else:
                return self._handle_error(response)
        except requests.exceptions.RequestException as e:
            return {"status": "fail", "message": f"Request failed: {str(e)}"}

    def _handle_error(self, response: requests.Response) -> dict:
        try:
            error_response = response.json()
            return {
                "status": error_response.get("status", "fail"),
                "message": error_response.get("message", "Unknown error occurred."),
            }
        except ValueError:
            return {"status": "fail", "message": "Invalid response from the server."}
