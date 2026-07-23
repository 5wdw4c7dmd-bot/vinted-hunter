from bs4 import BeautifulSoup
import re


def parse_items(html):

    soup = BeautifulSoup(html, "lxml")

    items = []
    seen = set()

    products = soup.select("[data-testid^='product-item-id']")

    for product in products:

        a = product.select_one("a[href*='/items/']")

        if not a:
            continue

        href = a.get("href", "")

        if href.startswith("/"):
            href = "https://www.vinted.cz" + href

        m = re.search(r"/items/(\d+)", href)

        if not m:
            continue

        item_id = m.group(1)

        if item_id in seen:
            continue

        seen.add(item_id)

        title = a.get("title", "").strip().lower()

        if not title:
            title = product.get_text(" ", strip=True).lower()

        # DEBUG
        print("")
        print("========================================")
        print("PARSER TITLE:")
        print(title)
        print("========================================")

        # Cena
        price = None

        price_el = product.select_one("[data-testid$='price-text']")

        if price_el:

            txt = (
                price_el.get_text(" ", strip=True)
                .replace("\xa0", "")
                .replace("Kč", "")
                .replace(",", ".")
            )

            m2 = re.search(r"(\d+(?:\.\d+)?)", txt)

            if m2:
                price = float(m2.group(1))

        if price is None:
            continue

        # Obrázek
        image = ""

        img = product.select_one("img")

        if img:

            image = img.get("src", "")

            if not image:
                srcset = img.get("srcset", "")
                if srcset:
                    image = srcset.split(",")[0].split(" ")[0]

        items.append(
            {
                "id": item_id,
                "url": href,
                "text": title,
                "price": price,
                "image": image,
            }
        )

    return items