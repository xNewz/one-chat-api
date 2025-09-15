import re
from typing import Optional

import requests

DEFAULT_TIMEOUT = (5, 15)


class MessageSender:
    def __init__(self, authorization_token: str):
        if authorization_token.startswith("Bearer "):
            authorization_token = authorization_token.replace("Bearer ", "", 1)
        self.authorization_token = authorization_token
        self.base_url = "https://chat-api.one.th/message/api/v1/push_message"
        self.headers = {
            "Authorization": f"Bearer {authorization_token}",
            "Content-Type": "application/json",
        }

    def send_message(
        self,
        to: str,
        bot_id: str,
        message: Optional[str],
        custom_notification: Optional[str] = None,
    ) -> dict:
        payload = {"to": to, "bot_id": bot_id, "type": "text", "message": message}
        if custom_notification:
            payload["custom_notification"] = custom_notification

        try:
            response = requests.post(
                self.base_url, headers=self.headers, json=payload, timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 200:
                return response.json()
            else:
                return self._handle_error(response)
        except requests.exceptions.RequestException as e:
            return {"status": "fail", "message": f"Request failed: {str(e)}"}

    def send_template(
        self,
        to: str,
        bot_id: str,
        template: Optional[list],
        custom_notification: Optional[str] = None,
    ) -> dict:
        payload = {"to": to, "bot_id": bot_id, "type": "template", "elements": template}
        if custom_notification:
            payload["custom_notification"] = custom_notification

        try:
            response = requests.post(
                self.base_url, headers=self.headers, json=payload, timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 200:
                return response.json()
            else:
                return self._handle_error(response)
        except requests.exceptions.RequestException as e:
            return {"status": "fail", "message": f"Request failed: {str(e)}"}

    def send_file(
        self,
        to: str,
        bot_id: str,
        file_path: Optional[str],
        custom_notification: Optional[str] = None,
    ) -> dict:
        data = {
            "to": to,
            "bot_id": bot_id,
            "type": "file",
        }

        if custom_notification:
            data["custom_notification"] = custom_notification

        headers = {k: v for k, v in self.headers.items() if k.lower() != "content-type"}

        if file_path is None:
            return {"status": "fail", "message": "file_path is required"}

        with open(file_path, "rb") as file:
            files = {
                "file": (file_path, file),
            }

            try:
                response = requests.post(
                    self.base_url,
                    headers=headers,
                    data=data,
                    files=files,
                    timeout=DEFAULT_TIMEOUT,
                )

                if response.status_code == 200:
                    return response.json()
                else:
                    return self._handle_error(response)
            except requests.exceptions.RequestException as e:
                return {"status": "fail", "message": f"Request failed: {str(e)}"}

    def send_webview(
        self,
        to: str,
        bot_id: str,
        url: Optional[str],
        custom_notification: Optional[str] = None,
    ):
        if not url or not re.match(r"^(http|https)://", url):
            return {
                "status": "fail",
                "message": "Please specify a protocol (http or https) in the URL.",
            }

        payload = {
            "to": to,
            "bot_id": bot_id,
            "type": "web",
            "url": url,
        }

        if custom_notification:
            payload["custom_notification"] = custom_notification

        try:
            response = requests.post(
                self.base_url, headers=self.headers, json=payload, timeout=DEFAULT_TIMEOUT
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
