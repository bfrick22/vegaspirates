import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def wait_for(condition_function, timeout=15):
    start_time = time.time()
    while time.time() < start_time + timeout:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )


class wait_for_page_load(object):
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    def __enter__(self):
        self.old_page = self.driver.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.driver.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded, self.timeout)


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
        self.repo_steps('Verifing page title')
        assert self.get_title() == self.page_title, "Couldn't validate page title.  Found {0} EXPECTED {1}".format(
            self.get_title(),
            self.page_title
        )

    def get(self):
        """Perform page tests/operations"""
        pass


class HomePage(Page):
    page_title = "Las Vegas Raiders! | Home"

    @classmethod
    def get_page_title(cls):
        return cls.page_title

    def get(self):
        self.repo_steps("Open page")
        self.open()
        self.verify_page_title()


class Login(Page):
    page_title = "Las Vegas Raiders! | Account"

    def login_form(self):
        username = self.driver.find_element_by_id("id_login")
        password = self.driver.find_element_by_id("id_password")
        submit = self.driver.find_element_by_xpath("/html/body/div[1]/form/button")
        username.send_keys("test")
        password.send_keys("test")
        with wait_for_page_load(self.driver):
            submit.click()

        # new title should be homepage tilte
        self.page_title = HomePage.get_page_title()
        self.verify_page_title()


    def get(self):
        self.open()
        self.verify_page_title()
        self.repo_steps("Logging user in")
        self.login_form()
