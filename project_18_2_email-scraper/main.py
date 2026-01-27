import re
from typing import Final
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Regex used for finding e-mails in text
EMAIL_REGEX: Final[
    str
] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class Browser:
    def __init__(self):
        print("Starting up browser...")
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")

        self.browser = webdriver.Chrome(options=self.chrome_options)

    def open_page(self, url: str):
        print(f"Opening browser...")
        self.browser.get(url)

    def close_browser(self):
        print(f"Closing browser...")
        self.browser.quit()

    def scrape_emails(self, url: str):
        print(f'Scraping: "{url}" for emails')
        self.open_page(url)

        WebDriverWait(self.browser, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        page_source: str = self.browser.page_source

        list_of_emails: set = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())

        return list_of_emails


def main():
    browser = Browser()
    emails: set = browser.scrape_emails(
        "https://randomlists.com/email-addresses?qty=50"
    )

    for i, email in enumerate(emails, start=1):
        print(i, email, sep=": ")

    browser.close_browser()


if __name__ == "__main__":
    main()
