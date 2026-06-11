from automation.browser import open_browser
from automation.login import login
from automation.navigation import open_create_notice
from automation.notice_form import fill_notice_form

playwright, browser, page = open_browser()

login(page)

open_create_notice(page)

fill_notice_form(page)

input("Review Form Then Press Enter To Close...")

browser.close()
playwright.stop()