from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddGroup():
    def setup_method(self):
        self.wd = webdriver.Chrome()
        self.wd.set_window_size(1592, 1025)
        self.vars = {}

    def teardown_method(self):
        self.wd.quit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element(By.CSS_SELECTOR, "[name=new]").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys("seleniumgroup")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys("header")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys("footer")
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def logout(self, wd):
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element(By.LINK_TEXT, "group page").click()

    def test_test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)










