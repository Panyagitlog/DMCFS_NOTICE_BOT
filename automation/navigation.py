def open_create_notice(page):

    print("Opening Notice Menu...")

    page.locator(
        "div"
    ).filter(
        has_text="Notice"
    ).nth(4).click()

    page.wait_for_timeout(2000)

    print("Opening Create Notice...")

    page.get_by_role(
        "link",
        name="Create Notice"
    ).click()

    page.wait_for_timeout(3000)

    print("Create Notice Page Opened")