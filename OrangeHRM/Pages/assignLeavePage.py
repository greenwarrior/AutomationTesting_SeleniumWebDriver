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
        self.employee_name = self.driver.find_element_by_id(Locators.employee_name_textbox_id).send_keys(emp_name)

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

    def entitlement_leave_type(self, select, value):
        driver = self.driver
        entitlementType = UtilitiesScript(driver)
        entitlementType.selectDropdown(select, value)

    def assign_leave_comments(self, assign_leave_comments):
        self.driver.find_element_by_id(Locators.leave_comment_textarea).send_keys(assign_leave_comments)
        time.sleep(5)
        #self.driver.find_element_by_id(Locators.leave_assign_button).click()

    def assign_leave_details(self, e_name, e_leave_type, e_leave_value, e_date1, e_date2, e_comments):
        self.assign_leave_emp_name(e_name)
        self.entitlement_leave_type(e_leave_type, e_leave_value)
        self.assign_leave_select_dates(e_date1, e_date2, )
        self.assign_leave_comments(e_comments)




    def assign_leave_successful(self):
        driver = self.driver
        time.sleep(5)
        name = driver.find_element_by_id(Locators.employee_name_textbox_id)
        l = self.driver.find_element_by_css_selector("#leaveBalance_details_link")
        link = l.get_attribute("innerHTML")
        self.driver.find_element_by_id(Locators.leave_assign_button).click()
        try:
            # assert ((driver.find_element_by_xpath("//*[@id='assign-leave']/div[1]/h1[contains(text(),'Assign Leave')]")) and (name.get_attribute("value") == TestData.emp_name))
            assert driver.find_element_by_xpath(
                "//*[@id='assign-leave']/div[1]/h1[contains(text(),'Assign Leave')]")
            print("ASSERT PASS -> LEAVE ASSIGNED SUCCESSFULLY! ")
        except Exception as e:
            print("Other Reason: Leave not assigned")


    def  assign_leave_overlapping(self):
        driver = self.driver
        time.sleep(5)
        name = driver.find_element_by_id(Locators.employee_name_textbox_id)
        l = self.driver.find_element_by_css_selector("#leaveBalance_details_link")
        link = l.get_attribute("innerHTML")
        self.driver.find_element_by_id(Locators.leave_assign_button).click()
        try:
             assert driver.find_element_by_css_selector("#content > div.box.single > div.head > h1").get_attribute("innerHTML") == "Overlapping Leave Request Found"
             print("ASSERT PASS -> OVERLAPPING LEAVE REQUEST")
        except Exception as e:
            print("ASSERT FAIL -> OVERLAPPING NOT TRACKED!")


    def assign_insufficient_leavebalance_cancel(self):
        driver = self.driver
        time.sleep(5)
        name = driver.find_element_by_id(Locators.employee_name_textbox_id)
        l = self.driver.find_element_by_css_selector("#leaveBalance_details_link")
        link = l.get_attribute("innerHTML")
        current_leave= self.get_current_leave_balance(link)


        self.driver.find_element_by_id(Locators.leave_assign_button).click()
        driver.find_element_by_xpath("//*[@id='leaveBalanceConfirm']/div[1]/h3[contains(text(),'OrangeHRM - Confirm Leave Assignment')]")
        driver.find_element_by_css_selector("#confirmCancelButton").click()
        time.sleep(5)
        new_leave = self.get_current_leave_balance(link)
        try:
            assert new_leave  == current_leave
            print("ASSERT BALANCE ->  INSUFFICIENT BALANCE  - Cancelled " + str(new_leave) + "   " + str(current_leave))
        except Exception as e:
            print("ASSERT FAIL -> INSUFFICIENT BALANCE NOT TRACKED")

    def assign_insufficient_leavebalance_confirm(self):
        driver = self.driver
        time.sleep(5)
        name = driver.find_element_by_id(Locators.employee_name_textbox_id)
        l = self.driver.find_element_by_css_selector("#leaveBalance_details_link")
        link = l.get_attribute("innerHTML")
        current_leave= self.get_current_leave_balance(link)


        self.driver.find_element_by_id(Locators.leave_assign_button).click()
        driver.find_element_by_xpath("//*[@id='leaveBalanceConfirm']/div[1]/h3[contains(text(),'OrangeHRM - Confirm Leave Assignment')]")
        driver.find_element_by_css_selector("#confirmOkButton").click()
        time.sleep(5)
        new_leave = self.get_current_leave_balance(link)

        try:
            assert new_leave  <= 0
            print("ASSERT BALANCE ->  INSUFFICIENT BALANCE  - Confirmed  " + str(new_leave) )
        except Exception as e:
            print("ASSERT FAIL -> INSUFFICIENT BALANCE NOT TRACKED")


        ###########################################################################################################
        # CLEAN ME !!!! Unused  methods                                                                                  #
        ###########################################################################################################
    def assign_leave_insufficient_balance(self):
        leave_balance_message = self.driver.find_element_by_css_selector("#leaveBalanceConfirm > div.modal-body > p:nth-child(1).gettext()")


    def get_current_leave_balance(self, strip_text):
        driver = self.driver
        leave_balance_before = UtilitiesScript(driver)
        leave_1 = leave_balance_before.strip_texts(strip_text)
        current_leave = float(leave_1)
        time.sleep(1)
        return current_leave

    #################################################################################
    #   DIV for error message
    #  css selector: #content > div > div.head
    #
    #   H1 Error text
    #  css selector: #content > div > div.head > h1
    #  xpath: //*[@id="content"]/div/div[1]/h1
    #
    #    Error Message
    #    css selector: #content > div > div.inner > div
    #    xpath: //*[@id="content"]/div/div[2]/div
    #
    #   "
    #    An internal error occurred. Please contact your system administrator.
    #      "
