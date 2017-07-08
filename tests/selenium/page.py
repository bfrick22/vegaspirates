from selenium import webdriver
from selenium.webdriver.common.by import By


class Page(object):
    page_title = ""

    def __init__(self, driver, base_url='http://localhost:8000'):
        self.driver = driver
        self.base_url = base_url

    @staticmethod
    def repo_steps(message):
        print(message)

    def get_title(self):
        return self.driver.title

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self, url=""):
        url = self.base_url + url
        self.driver.get(url)

    def verify_page_title(self):
        assert self.get_title() == self.page_title, "Couldn't validate page title.  Found {0} EXPECTED {1}".format(
            self.get_title(),
            self.page_title
        )

    def get(self):
        """Perform page tests/operations"""
        pass


class HomePage(Page):
    page_title = "Las Vegas Raiders! | Home"

    def get(self):
        self.repo_steps("Open page")
        self.open()
        self.verify_page_title()


class Login(Page):
    page_title = "Las Vegas Raiders! | Account"

    def get(self):
        self.repo_steps("Logging user in")
        self.open()
        self.verify_page_title()
