from playwright.sync_api import sync_playwright


def start_bot():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://lmsdmcfs.bterp.org/#/loginpage"
        )

        print("Login Page Opened")

        input("Press Enter To Close...")

        browser.close()