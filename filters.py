from config import BLOCKED_WORDS
from product_matcher import match_product


def check_item(item):

    text = item["text"].lower()

    result = {
        "ok": False,
        "reason": "",
        "product": None,
        "limit": None,
        "priority": 0,
        "set": None,
        "favorite": False,
        "matched_alias": None,
    }

    # Musí být nový
    if (
        "nový s visačkou" not in text
        and "nový bez visačky" not in text
    ):
        result["reason"] = "Produkt není nový"
        return result

    # Blacklist
    for word in BLOCKED_WORDS:

        if word.lower() in text:

            result["reason"] = f"Blacklist ({word})"
            return result

    # Rozpoznání produktu
    product = match_product(text)

    if product is None:

        result["reason"] = "Produkt není podporovaný"
        return result

    result["product"] = product["name"]
    result["matched_alias"] = product["matched_alias"]
    result["limit"] = product["limit"]
    result["priority"] = product["priority"]
    result["set"] = product["set"]
    result["favorite"] = product["favorite"]

    # Bonus za Pokémon Center
    if "pokemon center" in text:
        result["priority"] += 30

    # Bonus za sealed
    if "sealed" in text:
        result["priority"] += 15

    # Bonus za factory sealed
    if "factory sealed" in text:
        result["priority"] += 20

    # Bonus za oblíbený Pokémon set
    if result["favorite"]:
        result["priority"] += 30

    # Cena
    if item["price"] > result["limit"]:

        result["reason"] = (
            f"Cena {item['price']} Kč > limit {result['limit']} Kč"
        )

        return result

    result["ok"] = True

    # Důvod
    if result["set"]:

        result["reason"] = (
            f"{result['product']} | {result['set']}"
        )

    else:

        result["reason"] = (
            f"{result['product']}"
        )

    return result