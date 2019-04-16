import os
import time
import pytest
from selenium import webdriver
browser = os.getenv('BROWSER')
environment = os.getenv('ENVIRONMENT')


class TestGooglePage():

    @classmethod
    def setup_class(cls):
        "Runs once per class"

    @classmethod
    def teardown_class(cls):
        "Runs at end of class"
        # driver.quit()

    def setup(self):
        time.sleep(5)
        global driver
        # if "local" in environment:
        #     if "chrome" in browser:
        #         driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        #     if "firefox" in browser:
        #         driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        # else:
        #     driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={"browserName": browser})
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={"browserName": browser})

        driver.get("https://www.google.com.ua/")
        

    def teardown(self):
        # driver.close()
        driver.quit()

    # Tests
    def test_logo_is_present(self):
        time.sleep(5)
        google_logo = driver.find_element_by_xpath("//*[@id=\"hplogo\"]")
        assert self.is_element_exists(google_logo)

    def test_Pass(self):
        time.sleep(5)
        google_logo = driver.find_element_by_xpath("//*[@id=\"hplogo\"]")
        assert self.is_element_exists(google_logo)

    # Helper function
    def is_element_exists(self, element):
        try:
            if element is not None:
                return True
        except NoSuchElementException:
            return False