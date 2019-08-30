from selenium import webdriver
import time
import HtmlTestRunner
import unittest
import sys
import os
import re
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from OrangeHRM.Pages.loginPage import LoginPage
from OrangeHRM.Pages.assignLeavePage import AssignLeave
from OrangeHRM.Pages.utilities import UtilitiesScript
from OrangeHRM.Locators.testData import TestData
from OrangeHRM.Locators.locators import Locators


class LeaveTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_login(self):
        target_page = UtilitiesScript(self.driver)
        target_page.launch_target_page1(TestData.login_url, TestData.login_browser_title)
        login = LoginPage(self.driver)
        login.enter_username(TestData.admin_username)
        login.enter_password(TestData.admin_password)
        login.click_login()
        time.sleep(1)

    def test_02_Assign_leave_page(self):
        driver = self.driver
        driver.get(TestData.assign_leave_url)
        print(driver.current_url)
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()

    def test_03_assign_leaves_successful(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details(TestData.emp_name, TestData.leave_type,
                                               TestData.leave_type_value, TestData.date11,
                                               TestData.date12, TestData.leave_comments)
        assign_emp_leaves.assign_leave_successful()
        time.sleep(1)

    def test_04_assign_leave_overlapping(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details(TestData.emp_name, TestData.leave_type,
                                               TestData.leave_type_value, TestData.date21,
                                               TestData.date22, TestData.leave_comments)
        assign_emp_leaves.assign_leave_overlapping()
        time.sleep(1)

    def test_05_assign_leave_insufficient_cancel(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details(TestData.emp_name, TestData.leave_type,
                                               TestData.leave_type_value, TestData.date31,
                                               TestData.date32, TestData.leave_comments)
        assign_emp_leaves.assign_insufficient_leavebalance_cancel()
        time.sleep(1)

    def test_06_assign_leave_insufficient_confirm(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details(TestData.emp_name, TestData.leave_type,
                                               TestData.leave_type_value, TestData.date31,
                                               TestData.date32, TestData.leave_comments)
        assign_emp_leaves.assign_insufficient_leavebalance_confirm()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        #cls.driver.quit()
        print("Test Completed")


# To run without unittest
if __name__ == '__main__':
    print('HTMLTestRunner')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Learn/SeleniumProjects/OrangeHRM/Reports"))

"""

     def test_03_assign_leaves_successful(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details(TestData. emp_name, Locators.leave_types_dropdown, TestData.leave_type_option_value,TestData.leave_from_date,TestData.leave_to_date,TestData.leave_comments)
        assign_emp_leaves.assign_leave_successful()
        time.sleep(1)
        
    def test_04_assign_leave_overlapping(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details()
        assign_emp_leaves.assign_leave_overlapping()
        time.sleep(1)


    def test_05_assign_leave_insufficient_balance(self):
        driver = self.driver
        assign_emp_leaves = AssignLeave(driver)
        assign_emp_leaves.assign_leave_module()
        assign_emp_leaves.assign_leave_details()
        assign_emp_leaves.assign_leave_insufficient_leavebalance()
        time.sleep(1)
"""


