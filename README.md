<div align="center">

# OneChat Python Library

[![Build Status](https://img.shields.io/github/actions/workflow/status/xnewz/one-chat-api/publish.yml?style=flat-square)](https://github.com/xnewz/one-chat-api/actions)
[![PyPI - Version](https://img.shields.io/pypi/v/one-chat-api?style=flat-square)](https://pypi.org/project/one-chat-api/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/one-chat-api?style=flat-square)](https://pypi.org/project/one-chat-api/)
[![PyPI - Downloads](https://static.pepy.tech/personalized-badge/one-chat-api?period=total&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=GREEN&left_text=downloads)](https://pepy.tech/project/one-chat-api)
[![GitHub License](https://img.shields.io/github/license/xnewz/one-chat-api?style=flat-square)](https://github.com/xnewz/one-chat-api/blob/main/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/xnewz/one-chat-api?style=social)](https://github.com/xnewz/one-chat-api)

**A robust, elegant, and fully typed Python client for integrating with the OneChat API.**

</div>

---

## 📖 Overview

The **OneChat Python Library** provides a streamlined and developer-friendly interface for interacting with the OneChat platform. Whether you need to send direct messages, broadcast announcements, share files, or build interactive chatbot experiences, this library simplifies the integration process.

### ✨ Key Features

- 💬 **Messaging:** Send text, template, and quick-reply messages to users or groups.
- 📢 **Broadcasting:** Seamlessly send messages to multiple recipients at once.
- 📁 **Media & Files:** Share images, documents, and other files with ease.
- 📍 **Location & Stickers:** Send geographical coordinates and platform stickers.
- 🎠 **Interactive UI:** Deploy Image Carousels and WebViews for rich user experiences.
- 👥 **Audience Management:** Fetch, list, and manage friends and group IDs dynamically.

---

## 🚀 Installation

Install the library directly from PyPI using pip:

```bash
pip install one-chat-api
```

---

## 🛠️ Quick Start

### 1. Initialization
Before calling any API endpoints, initialize the library with your credentials.

```python
from one_chat import init

init(
    authorization="YOUR_AUTHORIZATION_TOKEN", # Replace with your Bearer token
    to="DEFAULT_RECIPIENT_ID",                # Default user or group ID
    bot_id="YOUR_BOT_ID"                      # Your registered Bot ID
)
```

*(Alternatively, import all functions at once: `from one_chat import *`)*

---

### 2. Core Capabilities

#### Send a Message
Send a basic text message to the default recipient or a specific user/group.

```python
from one_chat import send_message

response = send_message(message="Hello from OneChat!")
print("Send Message Response:", response)
```

#### Send a File or Image
Easily share documents or media files.

> [!TIP]
> You can send images using the `send_file` function, making it easier to share media files with your users!

```python
from one_chat import send_file

response = send_file(file_path="reports/results.csv")
print("Send File Response:", response)
```

#### Send a WebView
Trigger a webview inside the chat client for interactive web content.

> [!IMPORTANT]
> The URL must include the full protocol (`http://` or `https://`).

```python
from one_chat import send_webview

response = send_webview(url="https://google.com/")
print("Send Webview Response:", response)
```

#### Broadcast Messages
Send a message to a curated list of user IDs simultaneously.

> [!WARNING]
> Recipients must be a list of **User IDs** only. Group IDs are not supported in broadcasts.

```python
from one_chat import broadcast_message

response = broadcast_message(
    message="System Maintenance at 12:00 AM",
    to=["USER_ID_1", "USER_ID_2", "USER_ID_3"]
)
print("Broadcast Response:", response)
```

---

### 3. Rich Messaging

#### Send a Location
```python
from one_chat import send_location

response = send_location(
    latitude=13.7563, 
    longitude=100.5018, 
    address="Bangkok, Thailand"
)
```

#### Send a Sticker
```python
from one_chat import send_sticker

response = send_sticker(sticker_id="YOUR_STICKER_ID")
```

#### Send a Template Message
Interactive templates allow users to make choices quickly.
[Read more about templates in the official API docs](https://chat-develop.one.th/develop/docs/template/abouttemplate).

```python
from one_chat import send_template

response = send_template(
    template=[
        {
            "image": "https://example.com/cover.jpg",
            "title": "Welcome to our service",
            "detail": "Please select an option below",
            "choice": [
                {
                    "label": "Get Started",
                    "type": "text",
                    "payload": "ACTION_START"
                }
            ],
        }
    ]
)
```

#### Send Quick Replies
Prompt users with immediate contextual replies.
[Read more about quick replies](https://chat-develop.one.th/develop/docs/quickreply/aboutquickreply).

```python
from one_chat import send_quickreply

response = send_quickreply(
    message="What would you like to do next?",
    quick_reply=[
        {
            "label": "Register Now",
            "type": "text",
            "message": "I want to register",
            "payload": "CMD_REGISTER",
        }
    ],
)
```

#### Send Image Carousels
Display a horizontally scrollable list of images and actions.
[Read more about image carousels](https://chat-develop.one.th/develop/docs/carouselimage/aboutimagecarousel).

```python
from one_chat import send_image_carousel

response = send_image_carousel(
    elements=[
        {
            "type": "text",
            "image": "https://example.com/banner.jpg",
            "action": "hello",
            "payload": "Register",
            "sign": "false",
            "onechat_token": "false",
            "button": "Click Me",
        }
    ]
)
```

---

### 4. Audience Management

Retrieve lists of friends and groups associated with your bot.

```python
from one_chat import fetch_friends_and_groups, list_friend_ids, list_group_ids

# Get complete list of friends and groups
network = fetch_friends_and_groups()

# Extract just the IDs
friend_ids = list_friend_ids()
group_ids = list_group_ids()

print(f"Total Friends: {len(friend_ids)} | Total Groups: {len(group_ids)}")
```

*(Note: You can pass an explicit `"BOT_ID"` string to these functions to query a specific bot's network.)*

---

## 💻 Complete Example

A comprehensive example script is available here:

```python
from one_chat import init, send_message, send_location

def main():
    # Initialize the client
    init(
        authorization="YOUR_AUTHORIZATION_TOKEN",
        to="DEFAULT_RECIPIENT_ID",
        bot_id="YOUR_BOT_ID"
    )

    # Send a greeting
    send_message(message="Welcome to OneChat!")
    
    # Share a location
    send_location(latitude=13.7563, longitude=100.5018, address="Bangkok")

if __name__ == "__main__":
    main()
```

For more runnable examples, check the [`examples/`](./examples/) directory in the repository:
- `examples/quickstart.py` — Send a basic text message.
- `examples/broadcast.py` — Broadcast to a list of users.

---

## 🤝 Contributing

We welcome contributions from the community! 

Please read our [Contributing Guide](CONTRIBUTING.md) to get started. Be sure to also review our [Code of Conduct](CODE_OF_CONDUCT.md) and [Security Policy](SECURITY.md).

To run local checks before submitting a PR:
```bash
ruff check .
black --check .
mypy one_chat
pytest
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
