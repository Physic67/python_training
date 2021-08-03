# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.login(wd)
        self.fill_names(wd)
        self.add_address(wd)

        self.add_phones(wd)

    def add_phones(self, wd):
        # add telephones
        wd.find_element_by_name("home").send_keys("495-1234567")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("901-1234567")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()

    def add_address(self, wd):
        # add address
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Forks, Washington")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()

    def fill_names(self, wd):
        # add name
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Edward")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Vampire")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Kallen")

    def login(self, driver):
        # Login
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
