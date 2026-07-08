import requests

from config import BOT_TOKEN, CHAT_ID


def send(message, image=None):

    try:

        if image:

            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                data={
                    "chat_id": CHAT_ID,
                    "photo": image,
                    "caption": message,
                },
                timeout=30,
            )

        else:

            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": message,
                    "disable_web_page_preview": False,
                },
                timeout=30,
            )

        if response.status_code == 200:
            print("✅ Telegram OK")
        else:
            print(f"❌ Telegram chyba: {response.status_code}")
            print(response.text)

    except Exception as e:

        print(f"❌ Telegram Exception: {e}")