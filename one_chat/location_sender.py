import requests

class LocationSender:
    def __init__(self, authorization_token):
        self.authorization_token = authorization_token
        self.url = "https://chat-api.one.th/message/api/v1/push_message"

    def send_location(self, to, bot_id, latitude, longitude, address, custom_notification=None):
        headers = {
            "Authorization": f"Bearer {self.authorization_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "to": to,
            "bot_id": bot_id,
            "type": "location",
            "latitude": latitude,
            "longitude": longitude,
            "address": address,
            "custom_notification": custom_notification
        }

        response = requests.post(self.url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()  # Return error response for handling