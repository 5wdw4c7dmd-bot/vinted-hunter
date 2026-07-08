from datetime import datetime

from notifier import send


last_heartbeat_hour = None


def send_heartbeat(status):

    global last_heartbeat_hour

    now = datetime.now()

    if last_heartbeat_hour == now.hour:
        return

    last_heartbeat_hour = now.hour

    message = f"""💚 Vinted Hunter běží

🕒 Čas
{now.strftime("%d.%m.%Y %H:%M:%S")}

🔄 Kontrola
{status["checks"]}

📦 Alertů celkem
{status["alerts"]}

📦 Poslední produkt
{status["last_product"] or "-"}

💰 Poslední cena
{status["last_price"] or "-"}

⭐ Poslední score
{status["last_score"] or "-"}

⏰ Poslední kontrola
{status["last_check"]}
"""

    send(message)


def send_start_message():

    now = datetime.now()

    message = f"""🚀 Vinted Hunter spuštěn

🕒 {now.strftime("%d.%m.%Y %H:%M:%S")}

Bot byl úspěšně spuštěn a začíná sledovat Vinted.
"""

    send(message)