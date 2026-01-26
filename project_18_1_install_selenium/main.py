import time
from selenium import webdriver


class Browser:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def open_page(self, url: str):
        print(f"Opening browser...")
        self.browser.get(url)

    def close_browser(self):
        print(f"Closing browser...")
        self.browser.close()


if __name__ == "__main__":
    browser = Browser()

    browser.open_page("https://google.com")

    time.sleep(5)

    browser.close_browser()

    time.sleep(3)
