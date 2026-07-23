import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    try:

        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return []


def save_history(history):

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:

        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=2,
        )


def add_history(result, item, score):

    history = load_history()

    history.append({

        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "product": result["product"],

        "set": result["set"],

        "price": item["price"],

        "score": score,

        "url": item["url"],

    })

    # necháme jen posledních 1000 záznamů
    history = history[-1000:]

    save_history(history)