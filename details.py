from browser import browser


def get_details(url):

    page = browser.new_page()

    try:

        page.goto(url)

        page.wait_for_load_state("networkidle")

        seller = ""
        rating = ""
        reviews = ""
        description = ""

        body = page.locator("body").inner_text().lower()

        # zatím si jen uložíme celý text stránky
        description = body

        return {
            "seller": seller,
            "rating": rating,
            "reviews": reviews,
            "description": description,
        }

    finally:

        page.close()