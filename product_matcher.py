import re

from config import PRODUCTS, SETS, FAVORITE_SETS


def match_product(text):

    text = text.lower()

    best = None

    # Najdeme nejlepší shodu produktu
    for product in PRODUCTS:

        for alias in product["aliases"]:

            # Hledáme pouze celé slovo nebo frázi
            pattern = r"\b" + re.escape(alias) + r"\b"

            if re.search(pattern, text):

                if (
                    best is None
                    or len(alias) > len(best["matched_alias"])
                ):

                    best = {
                        "name": product["name"],
                        "matched_alias": alias,
                        "limit": product["limit"],
                        "priority": product["priority"],
                        "set": None,
                        "favorite": False,
                    }

    if best is None:
        return None

    # Najdeme Pokémon set
    for s in SETS:

        pattern = r"\b" + re.escape(s) + r"\b"

        if re.search(pattern, text):

            best["set"] = s.title()

            if s in FAVORITE_SETS:
                best["favorite"] = True

            break

    return best