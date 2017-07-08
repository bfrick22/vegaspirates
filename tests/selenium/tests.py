#!/usr/bin/python

import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from page import HomePage, Login


class BaseFirefoxSeleniumTests(unittest.TestCase):
    @staticmethod
    def status_report(driver_id, test_name, exit_status):
        """test_status_report function is used to report the status of a particular test."""
        pass

    @staticmethod
    def repro_steps(message):
        """repro_steps function prints/reports the reproduction step to figure out what failed."""
        print(str(message))

    def setUp(self):
        """setUp function sets up the Selenium test to run."""
        # create a Firefox profile that tells selenium what/where/how the browser runs in the env
        fp = webdriver.FirefoxProfile()

        # Add some preferences to the Firefox profile
        fp.set_preference('browser.cache.offline.enable', False)
        fp.set_preference('browser.cache.memory.enable', False)
        fp.update_preferences()

        # config capabilities
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True

        # set selenium webdriver
        self.driver = webdriver.Firefox(fp, capabilities=firefox_capabilities)

        # repo steps output
        self.repro_steps('Test {0} Reproduction Steps:'.format(self._testMethodName))

    def tearDown(self):
        """testDown function clears the webdriver to allow next test to run cleanly."""
        # report test status
        self.status_report(driver_id=self.driver.session_id,
                           test_name=self._testMethodName,
                           exit_status=sys.exc_info())

        # quit and clear driver
        self.driver.quit()

    def test_homepage(self):
        HomePage(self.driver, 'http://localhost:8000').get()

    def test_login(self):
        Login(self.driver, 'http://localhost:8000/accounts/login/').get()


if __name__ == '__main__':
    unittest.main()
