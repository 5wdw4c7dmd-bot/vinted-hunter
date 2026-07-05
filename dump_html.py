from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.vinted.cz/catalog?search_text=pokemon")

    print("Přijmi cookies.")
    input("Až uvidíš produkty, stiskni ENTER...")

    with open("vinted.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    print("HTML uloženo.")

    browser.close()
