# OneChat Python Library Documentation

## Overview

The OneChat Python library provides an interface for sending messages, broadcasting messages to multiple users, sending location information, and sending stickers through the OneChat API.

### Features

- Send Messages: Send messages to individual users or groups.
- Broadcast Messages: Send messages to multiple recipients at once.
- Send Locations: Share geographical locations with users.
- Send Stickers: Send sticker messages to users.

## Installation

To install the OneChat Python library, run the following command

```bash
pip install one-chat-api
```

## Usage

To use the OneChat library, follow these steps

### Import the Library

```python
from one_chat import init, send_message, broadcast_message, send_location, send_sticker
```

### Initialize the Library

Before using the functions, you need to initialize the library with your authorization token, default recipient, and bot id

```python
init(
    "YOUR_AUTHORIZATION_TOKEN",  # Replace with your token
    "DEFAULT_RECIPIENT_ID",      # Replace with user ID or group ID
    "YOUR_BOT_ID"                # Replace with your bot ID
)
```

### Send Messages

You can send a message to a specific user or group

```python
response = send_message(message="Hello One!")
print("Send Message response:", response)
```

### Broadcast Messages

To send a message to multiple recipients

> [!IMPORTANT]
> recipients must be a list of user IDs only !!! cannot be a group ID

```python
response = broadcast_message(message="Hello Multi!", to=["USER_ID_1", "USER_ID_2"])
print("Send Message Multi response:", response)
```

### Send Locations

To share a location

```python
response = send_location(latitude=13.7563, longitude=100.5018, address="Bangkok, Thailand")
print("Send Location Response:", response)
```

### Send Stickers

To send a sticker

```python
response = send_sticker(sticker_id="YOUR_STICKER_ID")
print("Send Sticker Response:", response)
```

## Example

Here’s a complete example of how to use the library

```python
from one_chat import *

def main():
    # Initialize OneChat with your token, recipient, and bot ID
    init(
        "YOUR_AUTHORIZATION_TOKEN",
        "DEFAULT_RECIPIENT_ID",  # Send to (One ID) or (Group ID)
        "YOUR_BOT_ID"  # Bot ID
    )

    # Send a single message
    resp_msg = send_message(message="Hello One!")
    print("Send Message response:", resp_msg)

    # Broadcast a message to multiple users
    resp_msg_multi = broadcast_message(message="Hello Multi!", to=["USER_ID_1", "USER_ID_2"])
    print("Send Message Multi response:", resp_msg_multi)

    # Send a location
    resp_location = send_location(latitude=13.7563, longitude=100.5018, address="Bangkok, Thailand")
    print("Send Location Response:", resp_location)

    # Send a sticker
    resp_sticker = send_sticker(sticker_id="YOUR_STICKER_ID")
    print("Send Sticker Response:", resp_sticker)

if __name__ == "__main__":
    main()
```