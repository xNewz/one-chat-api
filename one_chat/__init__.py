from typing import List, Optional, Union

# one_chat/__init__.py
from .one_chat import OneChat

__version__ = "0.4.2"

ONE_CHAT_INSTANCE: Optional[OneChat] = None
DEFAULT_TO: Optional[str] = None
DEFAULT_BOT_ID: Optional[str] = None


def init(authorization_token: str, to: Optional[str] = None, bot_id: Optional[str] = None):
    """Initialize a global OneChat instance and optional defaults.

    After calling, wrapper functions can use default `to` and `bot_id` values
    if not provided explicitly.
    """
    global ONE_CHAT_INSTANCE, DEFAULT_TO, DEFAULT_BOT_ID
    ONE_CHAT_INSTANCE = OneChat(authorization_token)
    DEFAULT_TO = to
    DEFAULT_BOT_ID = bot_id


def send_message(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    message: Optional[str] = None,
    custom_notification: Optional[str] = None,
):
    """Send a text message using the initialized client.

    Falls back to defaults provided in :func:`init` when not specified.
    """
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_message(to, bot_id, message, custom_notification)


def send_template(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    template: Optional[list] = None,
    custom_notification: Optional[str] = None,
):
    """Send a template message via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_template(to, bot_id, template, custom_notification)


def send_file(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    file_path: Optional[str] = None,
    custom_notification: Optional[str] = None,
):
    """Upload and send a file via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_file(to, bot_id, file_path, custom_notification)


def send_webview(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    url: Optional[str] = None,
    custom_notification: Optional[str] = None,
):
    """Send a webview (URL) message via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_webview(to, bot_id, url, custom_notification)


def broadcast_message(
    bot_id: Optional[str] = None,
    to: Optional[Union[List[str], str]] = None,
    message: Optional[str] = None,
):
    """Broadcast a message to multiple recipients using the global client.

    Accepts a single One ID or a list; a single string will be normalized to list.
    """
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    # Normalize recipients to a list of user IDs
    if to is None:
        if isinstance(DEFAULT_TO, str) and DEFAULT_TO:
            to = [DEFAULT_TO]
    elif isinstance(to, str):
        to = [to]

    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.broadcast_message(bot_id, to, message)


def send_location(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    latitude: Optional[str] = None,
    longitude: Optional[str] = None,
    address: Optional[str] = None,
    custom_notification: Optional[str] = None,
):
    """Send a location payload via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_location(
        to, bot_id, latitude, longitude, address, custom_notification
    )


def send_sticker(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    sticker_id: Optional[str] = None,
    custom_notification: Optional[str] = None,
):
    """Send a sticker via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_sticker(to, bot_id, sticker_id, custom_notification)


def send_quickreply(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    message: Optional[str] = None,
    quick_reply: Optional[list] = None,
    custom_notification: Optional[str] = None,
):
    """Send a message with quick replies via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_quickreply(to, bot_id, message, quick_reply, custom_notification)


def send_image_carousel(
    to: Optional[str] = None,
    bot_id: Optional[str] = None,
    elements: Optional[list] = None,
    custom_notification: Optional[str] = None,
):
    """Send an image carousel via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    to = to or DEFAULT_TO
    bot_id = bot_id or DEFAULT_BOT_ID

    if not to or not bot_id:
        raise ValueError(
            "Both 'to' and 'bot_id' must be provided either during "
            "initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.send_image_carousel(to, bot_id, elements, custom_notification)


def fetch_friends_and_groups(bot_id: Optional[str] = None):
    """Fetch friends and groups for the bot using the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    bot_id = bot_id or DEFAULT_BOT_ID

    if not bot_id:
        raise ValueError(
            "Bot ID must be provided either during initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.fetch_friends_and_groups(bot_id)


def list_all_friends(bot_id: Optional[str] = None):
    """Return full friend objects for the bot via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    bot_id = bot_id or DEFAULT_BOT_ID

    if not bot_id:
        raise ValueError(
            "Bot ID must be provided either during initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.list_all_friends(bot_id)


def list_friend_ids(bot_id: Optional[str] = None):
    """Return only friend One IDs for the bot via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    bot_id = bot_id or DEFAULT_BOT_ID

    if not bot_id:
        raise ValueError(
            "Bot ID must be provided either during initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.list_friend_ids(bot_id)


def list_all_groups(bot_id: Optional[str] = None):
    """Return full group objects for the bot via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    bot_id = bot_id or DEFAULT_BOT_ID

    if not bot_id:
        raise ValueError(
            "Bot ID must be provided either during initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.list_all_groups(bot_id)


def list_group_ids(bot_id: Optional[str] = None):
    """Return only group IDs for the bot via the global client."""
    if ONE_CHAT_INSTANCE is None:
        raise Exception(
            "OneChat is not initialized. Call init(authorization_token, to, bot_id) first."
        )

    bot_id = bot_id or DEFAULT_BOT_ID

    if not bot_id:
        raise ValueError(
            "Bot ID must be provided either during initialization or when calling this method."
        )

    return ONE_CHAT_INSTANCE.list_group_ids(bot_id)
