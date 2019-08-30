# Filename: homePage.py
# HomePage() Class
# 1. Create HomePage() class
# 2. Create a constructor with the argument 'driver' within the constructor
#    - Create the objects
# 3. Create the methods
#    - click_welcome(self)
#    - click_logout(self)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from OrangeHRM.Locators.locators import Locators

class HomePage():

    def __init__(self,driver):
        self.driver = driver


    def click_welcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id ).click()


    def click_logout(self):
        self.driver.find_element_by_link_text(Locators.logout_link_linkText).click()


