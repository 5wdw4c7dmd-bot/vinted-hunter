import requests
from config import TELEGRAM_TOKEN, CHAT_ID

def send(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    r = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": False
        }
    )

    print(r.status_code)
