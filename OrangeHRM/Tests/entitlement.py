import HtmlTestRunner
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
import time
from OrangeHRM.Pages.loginPage import LoginPage
from OrangeHRM.Locators.testData import TestData
from OrangeHRM.Locators.locators import Locators
from OrangeHRM.Pages.addEmpEntitlementPage import EmployeeEntitlementPage
from OrangeHRM.Pages.utilities import UtilitiesScript

class EntitlementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()




    def test_01_Login(self):
        ##############################################################
        # Login
        ##############################################################
        target_page = UtilitiesScript(self.driver)
        target_page.launch_target_page1(TestData.login_url, TestData.login_browser_title)
        login = LoginPage(self.driver)
        login.enter_username(TestData.admin_username)
        login.enter_password(TestData.admin_password)
        login.click_login()
        time.sleep(1)

    def test_02_Entitlement_module(self):
        entitlement = EmployeeEntitlementPage(self.driver)
        entitlement.leave_module()
        entitlement.entitlement_module()
        entitlement.entitlement_add_menu()

    def test_03_Entitlement_Details(self):
        ##############################################################
        # Entitlement Details
        ##############################################################
        entitlement = EmployeeEntitlementPage(self.driver)
        entitlement.add_employee_entitlement_details()
        time.sleep(1)

    def test_04_Entitlement_initial(self):
        entitlement = EmployeeEntitlementPage(self.driver)
        entitlement.entitlement_initial()

    def test_05_Entitlement_update(self):
        entitlement = EmployeeEntitlementPage(self.driver)
        #self.driver.find_element_by_id(Locators.entitlement_menu_id).click()
        #self.driver.find_element_by_id(Locators.entitlement_leave_menu_id).click()
        entitlement.entitlement_module()
        entitlement.entitlement_add_menu()
        time.sleep(1)
        entitlement.add_employee_entitlement_details()
        time.sleep(1)
        entitlement.entitlement_updated()

    def test_06_Entitlement_cancel(self):
        entitlement = EmployeeEntitlementPage(self.driver)
        #self.driver.find_element_by_id(Locators.entitlement_menu_id).click()
        #self.driver.find_element_by_id(Locators.entitlement_leave_menu_id).click()
        entitlement.entitlement_module()
        entitlement.entitlement_add_menu()
        time.sleep(1)
        entitlement.add_employee_entitlement_details()
        time.sleep(1)
        entitlement.entitlement_update_cancelled()


    def test_07_Search_entitlement(self):
        entitlement = EmployeeEntitlementPage(self.driver)
        entitlement.employee_entitlement_module()
        entitlement.search_entitlement()



    @classmethod
    def tearDownClass(cls):
       # cls.driver.close()
       # cls.driver.quit()
        print("Test Completed")


# To run without unittest

if __name__ == '__main__':
    print('HTMLTestRunner')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Learn/SeleniumProjects/OrangeHRM/Reports"))

"""      
    def test_07_Entitlement_confirm(self):
        entitlement = EmployeeEntitlementPage(self.driver)
        #self.driver.find_element_by_id(Locators.entitlement_menu_id).click()
        #self.driver.find_element_by_id(Locators.entitlement_leave_menu_id).click()
        entitlement.entitlement_module()
        entitlement.entitlement_add_menu()
        time.sleep(1)
        entitlement.add_employee_entitlement_details()
        time.sleep(1)
        entitlement.entitlement_update_confirm()

    def test_03_Add_first_employment_entitlement(self):
        driver = self.driver
        entitlement = EmployeeEntitlementPage(driver)

        entitlement.entitlement_add_emp_name(TestData.entitlement_emp_name)
        entitlement.entitlement_leave_type(Locators.entitlement_type_dropdown_id,
                                           Locators.entitlement_type_option_tagname,
                                           TestData.entitlement_type_option_value)
        entitlement.entitlement_add_leave_period(Locators.entitlement_period_dropdown,
                                                 Locators.entitlement_period_option_tagname,
                                                 TestData.entitlement_period_option_value)
        entitlement.entitlement_number_ofDays(TestData.entitlement_value)
        entitlement.entitlement_save_entry()
        entitlement.add_employee_entitlement()


    def test_04_Update_entitlement(self):
        driver = self.driver
        entitlement = EmployeeEntitlementPage(driver)
        entitlement.entitlement_module()
        time.sleep(1)

        entitlement.entitlement_add_emp_name(TestData.entitlement_emp_name)
        entitlement.entitlement_leave_type(Locators.entitlement_type_dropdown_id,
                                                  Locators.entitlement_type_option_tagname,
                                                  TestData.entitlement_type_option_value)
        entitlement.entitlement_add_leave_period(Locators.entitlement_period_dropdown,
                                                        Locators.entitlement_period_option_tagname,
                                                        TestData.entitlement_period_option_value)
        entitlement.entitlement_number_ofDays(TestData.entitlement_value)
        entitlement.entitlement_save_entry()
        entitlement.add_employee_entitlement()


    def test_05_Cancel_entitlement_update(self):
        driver = self.driver

        entitlement = EmployeeEntitlementPage(driver)
        entitlement.entitlement_module()
        time.sleep(1)

        entitlement.entitlement_add_emp_name(TestData.entitlement_emp_name)
        entitlement.entitlement_leave_type(Locators.entitlement_type_dropdown_id,
                                           Locators.entitlement_type_option_tagname,
                                           TestData.entitlement_type_option_value)
        entitlement.entitlement_add_leave_period(Locators.entitlement_period_dropdown,
                                                 Locators.entitlement_period_option_tagname,
                                                 TestData.entitlement_period_option_value)
        entitlement.entitlement_number_ofDays(TestData.entitlement_value)
        entitlement.entitlement_save_entry()
        entitlement.add_employee_entitlement()
"""













