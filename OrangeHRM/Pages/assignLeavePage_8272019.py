import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time
from selenium.webdriver.common.keys import Keys
from OrangeHRM.Locators.locators import Locators
from OrangeHRM.Pages.utilities import UtilitiesScript
from OrangeHRM.Locators.testData import TestData

class AssignLeave():

    def __init__(self,driver):
        self.driver = driver



    def assign_leave_module(self):
        self.driver.find_element_by_id(Locators.assign_leave_view_leave_module_menu_id).click()
        self.driver.find_element_by_id(Locators.leave_assign_leave_link).click()
        time.sleep(5)


    def assign_leave_emp_name(self, emp_name):
        self.employee_name =self.driver.find_element_by_id(Locators.employee_name_textbox_id).send_keys(emp_name)

    def assign_leave_select_dates(self,from_date,to_Date):
        start_date= self.driver.find_element_by_id(Locators.leave_from_date_datepicker)
        start_date.click()
        start_date.send_keys(from_date)
        start_date.send_keys(Keys.ENTER)
        time.sleep(5)
        end_date = self.driver.find_element_by_id(Locators.leave_to_date_datepicker)
        end_date.send_keys(Keys.CONTROL + "a")
        end_date.send_keys(to_Date)
        end_date.send_keys(Keys.ENTER)
        time.sleep(5)

    def entitlement_leave_type(self, select,  value):
        driver = self.driver
        entitlementType = UtilitiesScript(driver)
        entitlementType.selectDropdown(select,  value)

    def assign_leave_confirm(self, assign_leave_comments):
        self.driver.find_element_by_id(Locators.leave_comment_textarea).send_keys(assign_leave_comments)
        time.sleep(5)
        self.driver.find_element_by_id(Locators.leave_assign_button).click()

    def confirm_leave_assignment(self):
        driver = self.driver
        time.sleep(5)
        name = driver.find_element_by_id(Locators.employee_name_textbox_id)
        l = self.driver.find_element_by_css_selector("#leaveBalance_details_link")
        link = l.get_attribute("innerHTML")
        print(link)
        if link == "view details":
            try:
                assert ((driver.find_element_by_xpath("//*[@id='assign-leave']/div[1]/h1[contains(text(),'Assign Leave')]")) and (name.get_attribute("value") == TestData.emp_name))
                print(name.get_attribute("value"))
                print("Assert Pass: Leave assigned successfully")
            except Exception as e:
                print("Leave not assigned")
        elif link == "Balance not sufficient":
            try:
                assert driver.find_element_by_xpath("//*[@id='leaveBalanceConfirm']/div[1]/h3[contains(text(),'OrangeHRM - Confirm Leave Assignment')]")
                driver.find_element_by_id("confirmOkButton").click()
                print("Assert Pass : Insufficient Balance.")
            except Exception as e:
                print("Leave not assigned")
    ###########################################################################################################
    # CLEAN ME !!!! Unused  methods                                                                                  #
    ###########################################################################################################
    def assign_leave_insufficient_balance(self):
        leave_balance_message = self.driver.find_element_by_css_selector("#leaveBalanceConfirm > div.modal-body > p:nth-child(1).gettext()")
        print(leave_balance_message)

    def get_current_leave_balance(self,strip_text):
        driver = self.driver
        leave_balance_before = UtilitiesScript(driver)
        leave_1 = leave_balance_before.strip_texts(strip_text)
        float(leave_1)
        print(leave_1)
        time.sleep(5)

    ########### Not used
    def assign_leave_leave_type(self, leave_type):
        leave_types_dropdown = self.driver.find_element_by_id(Locators.leave_types_dropdown)
        leave_type_options = leave_types_dropdown.find_elements_by_tag_name(Locators.leave_type_dropdown_options)
        for option in leave_type_options:
            if option.get_attribute("value") == leave_type:
                option.click()
                break
        time.sleep(1)