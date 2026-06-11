from pathlib import Path


def fill_notice_form(page):

    print("Checking For Student...")

    page.locator("#flexCheckDefault1").check()

    page.wait_for_timeout(2000)

    print("For Student Selected")

    # ==========================
    # Scheme
    # ==========================

    print("Selecting Scheme...")

    page.get_by_role("combobox").first.click()

    page.get_by_role(
        "treeitem",
        name="WILP"
    ).click()

    page.wait_for_timeout(2000)

    # ==========================
    # Sector
    # ==========================

    print("Selecting Sector...")

    page.locator(
        "#j2 > .select2 > .selection > .select2-selection > .select2-selection__arrow"
    ).click()

    page.get_by_role(
        "treeitem",
        name="Automotive"
    ).click()

    page.wait_for_timeout(3000)

    # ==========================
    # Company
    # ==========================

    print("Selecting Company...")

    company_selected = False

    for attempt in range(5):

        try:

            company_dropdown = page.locator(
                "#j3 > .select2 > .selection > .select2-selection > .select2-selection__arrow"
            )

            company_dropdown.click()

            page.wait_for_timeout(2000)

            page.get_by_role(
                "treeitem",
                name="ADM JOINFLEX India Private"
            ).click()

            company_selected = True

            print("Company Selected")

            break

        except Exception:

            print(
                f"Company Not Loaded Yet... Retry {attempt + 1}"
            )

            page.wait_for_timeout(3000)

    if not company_selected:

        print("Company Selection Failed")

        return

    page.wait_for_timeout(2000)

    # ==========================
    # Topic
    # ==========================

    print("Filling Topic...")

    page.locator(
        "input[type='text']"
    ).fill(
        "Online Lecture"
    )

    # ==========================
    # Notice Category
    # ==========================

    print("Selecting Notice Category...")

    page.locator(
        "#select2-0"
    ).get_by_role(
        "combobox"
    ).click()

    page.get_by_role(
        "treeitem",
        name="General Notice"
    ).click()

    page.wait_for_timeout(1000)

    # ==========================
    # Importance
    # ==========================

    print("Selecting Importance...")

    page.locator(
        "#select2-1 > .select2 > .selection > .select2-selection > .select2-selection__arrow"
    ).click()

    page.get_by_role(
        "treeitem",
        name="Low"
    ).click()

    page.wait_for_timeout(1000)

    # ==========================
    # SMS Checkbox
    # ==========================

    print("Checking SMS Option...")

    page.locator(
        "#flexCheckDefault11"
    ).check()

    # ==========================
    # Notice Message
    # ==========================

    print("Loading Notice Template...")

    notice_file = Path(
        "templates/notice.txt"
    )

    notice_text = notice_file.read_text(
        encoding="utf-8"
    )

    print("Filling Notice Details...")

    page.locator(
        "textarea[type='text']"
    ).fill(
        notice_text
    )

    # ==========================
    # Expiry Date
    # ==========================

    print("Setting Expiry Date...")

    page.locator(
        "input[type='date']"
    ).fill(
        "2028-06-11"
    )

    page.wait_for_timeout(1000)

    print("\n===================================")
    print("NOTICE FORM FILLED SUCCESSFULLY")
    print("SAVE NOTICE NOT CLICKED")
    print("===================================\n")