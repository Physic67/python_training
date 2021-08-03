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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_untitled_test_case(self):
        driver = self.driver
        # Login
        driver.get("http://localhost/addressbook/edit.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Edward")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Vampire")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Kallen")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Forks, Washington")
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("495-1234567")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("901-1234567")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("Logout").click()


    

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
