import time
from datetime import datetime
from heartbeat import send_heartbeat, send_start_message
from browser import get_html, restart_browser
from parser import parse_items
from storage import load_seen, save_seen
from notifier import send
from filters import check_item
from score import calculate_score
from logger import log

from status import status

from config import (
    SEARCH_URLS,
    CHECK_INTERVAL,
    JACKPOT_LIMITS,
)

print("🚀 Vinted Hunter spuštěn")

log("===== BOT STARTED =====")

send_start_message()

seen = load_seen()
first_run = len(seen) == 0
send_heartbeat(status)

checks = 0

while True:

    try:

        checks += 1

        status["running"] = True
        status["checks"] = checks
        status["last_check"] = datetime.now().strftime("%H:%M:%S")

        if checks % 100 == 0:
            print("♻️ Restartuji Chromium...")
            log("Restart Chromium")
            restart_browser()

        alerts = 0
        total = 0

        # ----------------------------------
        # Projde všechny vyhledávací URL
        # ----------------------------------

        for search_url in SEARCH_URLS:

            if "lorcana" in search_url:
                print("\n🔵 Hledám Lorcanu...")
            else:
                print("\n🟡 Hledám Pokémon...")

            html = get_html(search_url)

            items = parse_items(html)

            print(f"📦 Nalezeno {len(items)} inzerátů")

            total += len(items)

            for item in items:

                if item["id"] in seen:
                    continue

                if first_run:
                    seen.add(item["id"])
                    continue

                result = check_item(item)

                print("")
                print("==========================================")
                print(item["text"])
                print(result["reason"])
                print("==========================================")

                if not result["ok"]:

                    log(
                        f"REJECT | {item['text']} | {result['reason']}"
                    )

                    seen.add(item["id"])
                    continue

                score = calculate_score(result)
                savings = round(result["limit"] - item["price"], 2)

                if (
                    result["product"] in JACKPOT_LIMITS
                    and item["price"] <= JACKPOT_LIMITS[result["product"]]
                ):
                    title = "💎💎💎 JACKPOT 💎💎💎"

                elif score >= 250:
                    title = "🚨🚨 TOP DEAL"

                elif score >= 180:
                    title = "🔥🔥 HOT DEAL"

                else:
                    title = "🔥 DEAL"

                print("")
                print(title)
                print(f"📦 {result['product']}")

                if result["set"]:
                    print(f"🎴 {result['set']}")

                print(f"⭐ SCORE: {score}")
                print(f"💰 {item['price']} Kč")
                print(item["url"])
                print("")

                status["alerts"] += 1
                status["last_product"] = result["product"]
                status["last_price"] = item["price"]
                status["last_score"] = score

                log(
                    f"FOUND | "
                    f"{result['product']} | "
                    f"{result['set']} | "
                    f"{item['price']} Kč | "
                    f"Score {score}"
                )

                message = f"""{title}

⭐ SCORE
{score}

📦 Produkt
{result['product']}
"""

                if result["set"]:
                    message += f"""

🎴 Set
{result['set']}
"""

                message += f"""

💰 Cena
{item['price']} Kč

🎯 Limit
{result['limit']} Kč

💸 Pod limitem
{savings} Kč

🔍 Rozpoznáno jako
{result['matched_alias']}

⭐ Priorita
{result['priority']}

📝 Název

{item['text']}

🔗 {item['url']}
"""

                send(
                    message,
                    item["image"],
                )

                alerts += 1
                seen.add(item["id"])

        save_seen(seen)

        first_run = False

        print(
            f"✅ Kontrola #{checks} | "
            f"Prohledáno: {total} | "
            f"Znám: {len(seen)} | "
            f"Alertů: {alerts}"
        )

    except Exception as e:

        print("❌ CHYBA:", e)
        log(f"ERROR | {e}")

    print(f"😴 Čekám {CHECK_INTERVAL} sekund...\n")

    time.sleep(CHECK_INTERVAL)