from typing import Any, Dict, List

# one_chat/friend_and_group_manager.py
import requests

DEFAULT_TIMEOUT = (5, 15)


class FriendAndGroupManager:
    """Fetch and extract friend/group information for a bot."""

    def __init__(self, authorization_token: str):
        """Initialize with Bearer token (with/without prefix)."""
        if authorization_token.startswith("Bearer "):
            authorization_token = authorization_token.replace("Bearer ", "", 1)
        self.authorization_token = authorization_token
        self.base_url = "https://chat-api.one.th/manage/api/v1/getlistroom"
        self.headers = {
            "Authorization": f"Bearer {self.authorization_token}",
            "Content-Type": "application/json",
        }

    def fetch_friends_and_groups(self, bot_id: str) -> Dict[str, Any]:
        """Call the API to fetch friends and groups for the given `bot_id`."""
        payload = {"bot_id": bot_id}
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

    def list_all_friends(self, bot_id: str) -> List[Dict[str, Any]]:
        """Return friend objects under the "list_friend" key, or an empty list."""
        try:
            response = self.fetch_friends_and_groups(bot_id)
            if response.get("status") == "success":
                return response.get("list_friend", [])
            return []
        except requests.exceptions.RequestException:
            return []

    def list_friend_ids(self, bot_id: str) -> List[str]:
        """Return only One IDs for all friends, or an empty list."""
        try:
            response = self.fetch_friends_and_groups(bot_id)
            if response.get("status") == "success":
                return [friend["one_id"] for friend in response.get("list_friend", [])]
            return []
        except requests.exceptions.RequestException:
            return []

    def list_all_groups(self, bot_id: str) -> List[Dict[str, Any]]:
        """Return group objects under the "list_group" key, or an empty list."""
        try:
            response = self.fetch_friends_and_groups(bot_id)
            if response.get("status") == "success":
                return response.get("list_group", [])
            return []
        except requests.exceptions.RequestException:
            return []

    def list_group_ids(self, bot_id: str) -> List[str]:
        """Return only group IDs for all groups, or an empty list."""
        try:
            response = self.fetch_friends_and_groups(bot_id)
            if response.get("status") == "success":
                return [group["group_id"] for group in response.get("list_group", [])]
            return []
        except requests.exceptions.RequestException:
            return []

    def _handle_error(self, response: requests.Response) -> dict:
        """Normalize API error responses to a consistent structure."""
        try:
            error_response = response.json()
            return {
                "status": error_response.get("status", "fail"),
                "message": error_response.get("message", "Unknown error occurred."),
            }
        except ValueError:
            return {"status": "fail", "message": "Invalid response from the server."}
