import os

from one_chat import broadcast_message, init


def main():
    token = os.environ.get("ONECHAT_TOKEN")
    bot = os.environ.get("ONECHAT_BOT_ID")
    users = (
        os.environ.get("ONECHAT_USERS", "").split(",") if os.environ.get("ONECHAT_USERS") else []
    )

    if not all([token, bot]) or not users:
        raise SystemExit("Please set ONECHAT_TOKEN, ONECHAT_BOT_ID, ONECHAT_USERS (comma sep)")

    # We don't set default recipient for broadcast usage
    init(token, None, bot)
    resp = broadcast_message(message="Hello everyone!", to=users)
    print(resp)


if __name__ == "__main__":
    main()
