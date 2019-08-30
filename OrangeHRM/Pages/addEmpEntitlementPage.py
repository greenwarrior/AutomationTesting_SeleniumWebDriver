import time
from selenium.webdriver.common.keys import Keys
from OrangeHRM.Locators.testData import TestData
from OrangeHRM.Locators.locators import Locators
from OrangeHRM.Pages.utilities import UtilitiesScript



class EmployeeEntitlementPage():

    def __init__(self,driver):
        self.driver = driver


    def leave_module(self):
        self.driver.find_element_by_id(Locators.assign_leave_view_leave_module_menu_id).click()

    def entitlement_module(self):
        self.driver.find_element_by_id(Locators.entitlement_menu_id).click()

    def entitlement_add_menu(self):
        self.driver.find_element_by_id(Locators.entitlement_leave_menu_id).click()
        time.sleep(2)

    def entitlement_add_emp_name(self, entitlement_emp_name):
        target_page = UtilitiesScript(self.driver)
        target_page.launch_target_page2(TestData.add_entitlement)
        self.driver.find_element_by_id(Locators.entitlement_leave_empname_input_id).send_keys(entitlement_emp_name)
        self.driver.find_element_by_id(Locators.entitlement_leave_empname_input_id).send_keys(Keys.ENTER)

    def entitlement_leave_type(self, select,  value):
        driver = self.driver
        entitlementType = UtilitiesScript(driver)
        entitlementType.selectDropdown(select,  value)

    def entitlement_add_leave_period(self,select,  value):
        driver = self.driver
        entitlementPeriod = UtilitiesScript(driver)
        entitlementPeriod.selectDropdown(select,  value)

    def entitlement_number_ofDays(self, num_days):
        self.driver.find_element_by_xpath(Locators.entitlement__days_input_xpath).send_keys(num_days)

    def entitlement_save_entry(self):
        self.driver.find_element_by_id(Locators.entitlement_save_button_id).click()
        time.sleep(5)

    def add_employee_entitlement_details(self):
        time.sleep(2)
        self.entitlement_add_emp_name(TestData.entitlement_emp_name)
        time.sleep(1)
        self.entitlement_leave_type(Locators.entitlement_type_dropdown_id, TestData.entitlement_type_option_value)
        time.sleep(1)
        self.entitlement_add_leave_period(Locators.entitlement_period_dropdown,TestData.entitlement_period_option_value)
        time.sleep(1)
        self.entitlement_number_ofDays(TestData.entitlement_value)

    def entitlement_initial(self):
        driver = self.driver
        self.entitlement_save_entry()
        time.sleep(5)
        try:
            assert driver.find_element_by_id("search_form").is_displayed()
            print("ASSERT PASS:-> INITIAL ENTITLEMENT.")

        except Exception as e:
            print("Assert Fail: Initial entitlement not added successfully.")


    def entitlement_updated(self,):
        driver = self.driver
        self.entitlement_save_entry()
        driver.find_element_by_id(Locators.entitlement_update_confirm_button_id).click()
        try:
            assert driver.find_element_by_xpath("//*[@id='leave-entitlementsSearch']/div[1]/h1[contains(text(),'Leave Entitlements')]")
            print("ASSERT PASS -> UPDATE CURRENT ENTITLEMENT.")
        except Exception as e:
            print("Assert Fail: Entitlement is not updated")

    def entitlement_update_cancelled(self,):
        driver = self.driver
        self.entitlement_save_entry()
        time.sleep(5)
        driver.find_element_by_id(Locators.entitlement_update_cancel_button_id).click()
        time.sleep(5)
        try:
            assert driver.find_element_by_xpath("//*[@id='add-leave-entitlement']/div[1]/h1[contains(text(),'Add Leave Entitlement')]")
            print("ASSERT PASS -> UPDATE ENTITLEMENT CANCELLED.")
        except Exception as e:
            print("Assert Fail: Entitlement should be cancelled")



    def employee_entitlement_module(self):
        driver = self.driver
        # Find the Employee Entitlement link and click
        self.driver.find_element_by_id(Locators.assign_leave_view_leave_module_menu_id).click()
        self.driver.find_element_by_id(Locators.entitlement_menu_id).click()
        self.driver.find_element_by_id("menu_leave_viewLeaveEntitlements").click()
        print("Searching employee entitlement! ")

    def search_entitlement(self):
        ########################################################################################
        # Search the added entitlement
        ########################################################################################
        self.driver.find_element_by_id(Locators.entitlement_leave_empname_input_id).click()
        self.driver.find_element_by_id(Locators.entitlement_leave_empname_input_id).send_keys(TestData.emp_name)
        self.driver.find_element_by_id(Locators.entitlement_leave_empname_input_id).send_keys(Keys.ENTER)
        time.sleep(2)
        self.entitlement_leave_type(Locators.entitlement_type_dropdown_id, TestData.entitlement_type_option_value)
        time.sleep(2)
        self.entitlement_add_leave_period(Locators.entitlement_period_dropdown, TestData.entitlement_period_option_value)
        time.sleep(2)
        self.driver.find_element_by_css_selector(Locators.entitlement_search_button_id).click()
        print("Searching employee entitlement! ")







