from typing import List, Optional

# one_chat/one_chat.py
from .broadcast_sender import BroadcastSender
from .get_friends_and_groups import FriendAndGroupManager
from .image_carousel_sender import ImageCarouselSender
from .location_sender import LocationSender
from .message_sender import MessageSender
from .quickreply_sender import QuickReplySender
from .sticker_sender import StickerSender


class OneChat:
    """High-level facade for OneChat API operations.

    This class aggregates specialized sender/managers to provide a simple API for
    common OneChat tasks such as sending messages, files, locations, stickers, quick
    replies, image carousels, broadcasting messages, and listing friends/groups.
    """

    def __init__(self, authorization_token: str):
        """Initialize a OneChat client.

        Parameters:
        - authorization_token: The Bearer token (with or without the
          leading "Bearer ").
        """
        self.message_sender = MessageSender(authorization_token)
        self.broadcast_sender = BroadcastSender(authorization_token)
        self.location_sender = LocationSender(authorization_token)
        self.sticker_sender = StickerSender(authorization_token)
        self.quick_reply_sender = QuickReplySender(authorization_token)
        self.image_carousel_sender = ImageCarouselSender(authorization_token)
        self.friends_and_groups = FriendAndGroupManager(authorization_token)

    def send_message(
        self,
        to: str,
        bot_id: str,
        message: Optional[str],
        custom_notification: Optional[str] = None,
    ):
        """Send a plain text message to a user.

        Parameters:
        - to: Recipient One ID.
        - bot_id: Bot ID performing the send.
        - message: Text content to send.
        - custom_notification: Optional custom notification text.
        """
        return self.message_sender.send_message(to, bot_id, message, custom_notification)

    def send_template(
        self,
        to: str,
        bot_id: str,
        template: Optional[list],
        custom_notification: Optional[str] = None,
    ):
        """Send a template message (elements payload).

        Parameters mirror :meth:`MessageSender.send_template`.
        """
        return self.message_sender.send_template(to, bot_id, template, custom_notification)

    def send_file(
        self,
        to: str,
        bot_id: str,
        file_path: Optional[str],
        custom_notification: Optional[str] = None,
    ):
        """Upload and send a file to a user.

        Parameters mirror :meth:`MessageSender.send_file`.
        """
        return self.message_sender.send_file(to, bot_id, file_path, custom_notification)

    def send_webview(
        self, to: str, bot_id: str, url: Optional[str], custom_notification: Optional[str] = None
    ):
        """Send a webview (URL) message after basic protocol validation."""
        return self.message_sender.send_webview(to, bot_id, url, custom_notification)

    def broadcast_message(self, bot_id: str, to: List[str], message: Optional[str]):
        """Broadcast a message to up to 100 recipients.

        Parameters mirror :meth:`BroadcastSender.broadcast_message`.
        """
        return self.broadcast_sender.broadcast_message(bot_id, to, message)

    def send_location(
        self,
        to: str,
        bot_id: str,
        latitude: Optional[str],
        longitude: Optional[str],
        address: Optional[str],
        custom_notification: Optional[str] = None,
    ):
        """Send a location payload with coordinates and address."""
        return self.location_sender.send_location(
            to, bot_id, latitude, longitude, address, custom_notification
        )

    def send_sticker(
        self,
        to: str,
        bot_id: str,
        sticker_id: Optional[str],
        custom_notification: Optional[str] = None,
    ):
        """Send a sticker by sticker ID."""
        return self.sticker_sender.send_sticker(to, bot_id, sticker_id, custom_notification)

    def send_quickreply(
        self,
        to: str,
        bot_id: str,
        message: Optional[str],
        quick_reply: Optional[list],
        custom_notification: Optional[str] = None,
    ):
        """Send a message with quick reply buttons."""
        return self.quick_reply_sender.send_quickreply(
            to, bot_id, message, quick_reply, custom_notification
        )

    def send_image_carousel(
        self,
        to: str,
        bot_id: str,
        elements: Optional[list],
        custom_notification: Optional[str] = None,
    ):
        """Send an image carousel composed of provided elements."""
        return self.image_carousel_sender.send_image_carousel(
            to, bot_id, elements, custom_notification
        )

    def fetch_friends_and_groups(self, bot_id: str):
        """Fetch lists of friends and groups for the given bot."""
        return self.friends_and_groups.fetch_friends_and_groups(bot_id)

    def list_all_friends(self, bot_id: str):
        """Return full friend objects as provided by the API."""
        return self.friends_and_groups.list_all_friends(bot_id)

    def list_friend_ids(self, bot_id: str):
        """Return a list of friend One IDs only."""
        return self.friends_and_groups.list_friend_ids(bot_id)

    def list_all_groups(self, bot_id: str):
        """Return full group objects as provided by the API."""
        return self.friends_and_groups.list_all_groups(bot_id)

    def list_group_ids(self, bot_id: str):
        """Return a list of group IDs only."""
        return self.friends_and_groups.list_group_ids(bot_id)
