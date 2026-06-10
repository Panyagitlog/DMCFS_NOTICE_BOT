from automation.browser import open_browser
from automation.login import login
from automation.navigation import open_create_notice

playwright, browser, page = open_browser()

login(page)

open_create_notice(page)

print("READY FOR INSPECTION")

input("DO NOT CLOSE. PRESS ENTER WHEN DONE...")

browser.close()
playwright.stop()