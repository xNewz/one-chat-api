# OneChat Python Library Documentation

## Overview

The OneChat Python library provides an interface for sending messages, broadcasting messages to multiple users, sending location information, sending stickers, and sending files through the OneChat API.

### Features

- Send Messages: Send messages to individual users or groups.
- Send Files: Send files to users for easy sharing.
- Send WebView: Send a webview to users for interactive content.
- Broadcast Messages: Send messages to multiple recipients at once.
- Send Locations: Share geographical locations with users.
- Send Stickers: Send sticker messages to users.
- Fetch Friends and Groups: Retrieve the complete list of friends and groups for a bot.
- List All Friends: Get a list of all friends associated with the bot.
- List Friend IDs: Retrieve the One IDs of all friends for easy identification.
- List All Groups: Get a list of all groups associated with the bot.
- List Group IDs: Retrieve the IDs of all groups for further actions.

## Installation

To install the OneChat Python library, run the following command

```bash
pip install one-chat-api
```

## Usage

To use the OneChat library, follow these steps

### Import the Library

```python
from one_chat import (
    init,
    send_message,
    send_file,
    broadcast_message,
    send_location,
    send_sticker,
    fetch_friends_and_groups,
    list_all_friends,
    list_friend_ids,
    list_all_groups,
    list_group_ids,
)
```

or you can import all functions at once

```python
from one_chat import *
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

### Send Files

You can send a file to a specific user or group

```python
response = send_file(file_path="results.csv")
print("Send File response:", response)
```

> [!TIP]
> You can now send images using the send_file function, making it easier to share media files with your users!

### Send WebView
```python
response = send_webview(url="https://google.com/")
print("Send Webview response:", response)
```

> [!IMPORTANT]
> You need to specify the Protocol (http:// or https://) in the URL

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

    # Send a file
    resp_file = send_file(file_path="results.csv")
    print("Send File response:", resp_file)

    # Send a webview
    resp_webview = send_webview(url="https://google.com/")
    print("Send Webview response:", resp_webview)

    # Broadcast a message to multiple users
    resp_msg_multi = broadcast_message(message="Hello Multi!", to=["USER_ID_1", "USER_ID_2"])
    print("Send Message Multi response:", resp_msg_multi)

    # Send a location
    resp_location = send_location(latitude=13.7563, longitude=100.5018, address="Bangkok, Thailand")
    print("Send Location Response:", resp_location)

    # Send a sticker
    resp_sticker = send_sticker(sticker_id="YOUR_STICKER_ID")
    print("Send Sticker Response:", resp_sticker)

    # Get a list of friends and groups
    friends_and_groups = fetch_friends_and_groups() # you can use fetch_friends_and_groups("BOT_ID") to get friends and groups of another bot
    print("Friends and Groups:", friends_and_groups)

    # Get a list of friends
    friends = list_all_friends() # you can use list_all_friends("BOT_ID") to get friends of another bot
    print("Friends:", friends)

    # Get the One ID of a friend
    one_id = list_friend_ids() # you can use list_friend_ids("BOT_ID") to get one id of a friend of another bot
    print("One ID of Friend:", one_id)

    # Get a list of groups
    groups = list_all_groups() # you can use list_all_groups("BOT_ID") to get groups of another bot
    print("Groups:", groups)

    # Get the group ID of a group
    group_id = list_group_ids() # you can use list_group_ids("BOT_ID") to get group id of a group of another bot
    print("Group ID of Group:", group_id)

if __name__ == "__main__":
    main()
```
