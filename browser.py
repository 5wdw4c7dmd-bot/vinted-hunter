from playwright.sync_api import sync_playwright

playwright = None
browser = None
page = None
current_url = None


def start_browser():

    global playwright
    global browser
    global page
    global current_url

    if page is not None:
        return

    print("🚀 Spouštím Chromium...")

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=True,
        args=[
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-background-networking",
            "--disable-background-timer-throttling",
            "--disable-renderer-backgrounding",
            "--no-sandbox",
        ],
    )

    page = browser.new_page()

    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)

    current_url = None


def get_html(url):

    global page
    global current_url

    try:

        start_browser()

        if current_url != url:

            page.goto(
                url,
                wait_until="domcontentloaded",
            )

            current_url = url

        else:

            page.reload(
                wait_until="domcontentloaded",
            )

        page.wait_for_timeout(2000)

        return page.content()

    except Exception as e:

        print("⚠️ Chromium spadlo:", e)

        restart_browser()

        page.goto(
            url,
            wait_until="domcontentloaded",
        )

        page.wait_for_timeout(2000)

        current_url = url

        return page.content()


def restart_browser():

    global playwright
    global browser
    global page
    global current_url

    print("♻️ Restartuji Chromium...")

    try:
        if page:
            page.close()
    except:
        pass

    try:
        if browser:
            browser.close()
    except:
        pass

    try:
        if playwright:
            playwright.stop()
    except:
        pass

    playwright = None
    browser = None
    page = None
    current_url = None

    start_browser()


def stop_browser():

    global page
    global browser
    global playwright

    try:
        if page:
            page.close()
    except:
        pass

    try:
        if browser:
            browser.close()
    except:
        pass

    try:
        if playwright:
            playwright.stop()
    except:
        pass