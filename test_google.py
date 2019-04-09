import os
import time
import pytest
from selenium import webdriver
browser = os.getenv('BROWSER')


class TestGooglePage():

    @classmethod
    def setup_class(cls):
        "Runs once per class"

    @classmethod
    def teardown_class(cls):
        "Runs at end of class"
        # driver.quit()

    def setup(self):
        global driver
        # driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={"browserName": browser})
        driver.get("https://www.google.com.ua/")
        

    def teardown(self):
        driver.close()

    # Tests
    def test_logo_is_present(self):
        google_logo = driver.find_element_by_xpath("//*[@id=\"hplogo\"]")
        assert self.is_element_exists(google_logo)

    def test_Fail(self):
        assert False

    # Helper function
    def is_element_exists(self, element):
        try:
            if element is not None:
                return True
        except NoSuchElementException:
            return False