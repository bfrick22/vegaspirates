from selenium import webdriver
from selenium.webdriver.common.by import By


class Page(object):
    def __init__(self, driver, base_url='http://localhost:8000'):
        self.driver = driver
        self.base_url = base_url

    def repo_steps(self, message):
        print(message)

    def get_title(self):
        return self.driver.title

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self, url="/"):
        url = self.base_url + url
        self.driver.get(url)

    def get(self):
        """Perform page tests/operations"""
        pass


class HomePage(Page):
    page_title = "Las Vegas Raiders!"

    def get(self):
        self.repo_steps("Open page")
        self.open()
        assert self.get_title() == self.page_title, "Title has changed.  Found {0} EXPECTED {1}".format(
            self.get_title(),
            self.page_title
        )
