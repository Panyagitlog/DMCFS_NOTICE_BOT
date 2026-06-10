from automation.config import *


def login(page):

    page.goto(LOGIN_URL)

    page.wait_for_timeout(3000)

    print("Login Page Opened")

    page.get_by_role(
        "textbox",
        name="Username"
    ).fill(USERNAME)

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill(PASSWORD)

    print("Credentials Filled")

    page.wait_for_timeout(2000)

    print("Clicking Login Button...")

    page.get_by_role(
        "button",
         name="Login"
    ).click()

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    page.wait_for_timeout(5000)

    print("Login Completed")