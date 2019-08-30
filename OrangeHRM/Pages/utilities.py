import re
from OrangeHRM.Locators.locators import Locators
from OrangeHRM.Locators.testData import TestData
from selenium.webdriver.support.ui import Select

class UtilitiesScript():

    def __init__(self,driver):
        self.driver = driver

    def launch_target_page1(self,url,browser_title):
        driver = self.driver
        driver.get(url)
        try:
            assert browser_title in driver.title
            print("Assert: Browser title - " + driver.title)

        except Exception as e:
            print("Assert Fail: Browser title - " + driver.title)

    def launch_target_page2(self,url):
        driver = self.driver
        try:
            assert url in driver.current_url
            print("Assert  Pass: Browser title - " + driver.current_url)
        except Exception as e:
            print("Assert Fail: Browser title - " + driver.current_url)

    def strip_texts(self,texts_to_strip):
        #element = self.driver.find_element_by_id("assignleave_leaveBalance")
        element = self.driver.find_element_by_id("assignleave_leaveBalance")
        element_tag_text = element.get_attribute("innerHTML")
        clean = re.compile('<.*?>')
        cleaned_text = re.sub(clean, '', element_tag_text)
        target_text = (cleaned_text.strip(texts_to_strip))
        #print(target_text)
        return target_text


    def selectDropdown(self,select_dropdown,  option_value):
        select = Select(self.driver.find_element_by_id(select_dropdown))
        select.select_by_value(option_value)


