from playwright.sync_api import sync_playwright

def response_listener(response):
    url = response.url

    if "api" in url:
        print(url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.on("response", response_listener)

    page.goto("https://www.vinted.cz/catalog?search_text=pokemon")

    input("Sroluj stránku dolů a pak Enter...")

    browser.close()