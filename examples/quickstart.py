import os

from one_chat import init, send_message


def main():
    token = os.environ.get("ONECHAT_TOKEN")
    to = os.environ.get("ONECHAT_TO")
    bot = os.environ.get("ONECHAT_BOT_ID")

    if not all([token, to, bot]):
        raise SystemExit("Please set ONECHAT_TOKEN, ONECHAT_TO, ONECHAT_BOT_ID env vars")

    init(token, to, bot)
    resp = send_message(message="Hello One!")
    print(resp)


if __name__ == "__main__":
    main()
