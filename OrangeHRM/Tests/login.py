from selenium import webdriver
import time
import HtmlTestRunner
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from OrangeHRM.Pages.loginPage import LoginPage
from OrangeHRM.Pages.homePage import HomePage
from OrangeHRM.Locators.testData import TestData
from OrangeHRM.Pages.utilities import UtilitiesScript


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_Launch_login_page(self):
        target_page = UtilitiesScript (self.driver)
        target_page.launch_target_page1(TestData.login_url,TestData.login_browser_title)

    def test_02_Login_valid_username(self):
        driver = self.driver

        driver.get(TestData.login_url)
        login = LoginPage(driver)
        login.enter_username(TestData.admin_username)
        login.enter_password(TestData.admin_password)
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        target_page = UtilitiesScript(driver)
        target_page.launch_target_page2(TestData.logout_url)
        time.sleep(2)

    def test_03_Login_invalid_username(self):
        driver = self.driver
        driver.get(TestData.login_url)
        login = LoginPage(driver)
        login.enter_username(TestData.admin_username_invalid)
        login.enter_password(TestData.admin_password)
        login.click_login()
        login.check_invalid_username_message()
        target_page = UtilitiesScript(driver)
        target_page.launch_target_page2(TestData.invalid_credential_url)
        time.sleep(2)

    def test__04_Login_incorrect_password(self):
        driver = self.driver
        driver.get(TestData.login_url)
        login = LoginPage(driver)
        login.enter_username(TestData.admin_username)
        login.enter_password(TestData.admin_password_invalid)
        login.click_login()
        target_page = UtilitiesScript(driver)
        target_page.launch_target_page2(TestData.invalid_credential_url)
        login.check_invalid_password_message()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

    # To run without unittest
if __name__ == '__main__':
    print('HTMLTestRunner')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Learn/SeleniumProjects/OrangeHRM/Reports"))
