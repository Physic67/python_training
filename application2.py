from selenium import webdriver

class Application2:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def add_phones(self, contact):
            wd = self.wd
            wd.find_element_by_name("home").send_keys(contact.homephone)
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobilephone)

    def save_contact(self):
            wd = self.wd
            wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_address(self, contact):
            wd = self.wd
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()

    def fill_names(self, contact):
            wd = self.wd
            wd.find_element_by_link_text("add new").click()
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def login(self, username, password):
            wd = self.wd
            wd.get("http://localhost/addressbook/")
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//input[@value='Login']").click()

    def destroy(self):
        self.wd.quit()