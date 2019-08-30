import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from OrangeHRM.Locators.locators import Locators

class LoginPage():

    #2
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(Locators.password_textbox_id ).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id ).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_button_id ).click()


    def check_invalid_username_message(self):
        # msg = self.driver.find_element_by_xpath("//*[@id='spanMessage'][contains(text(),'Invalid credentials123')]")
        msg = self.driver.find_element_by_xpath(Locators.invalidUsername_span_xpath + Locators.invalidUsername_span_message)



    def check_invalid_password_message(self):
        msg = self.driver.find_element_by_xpath(Locators.invalidUsername_span_xpath + Locators.invalidUsername_span_message)
