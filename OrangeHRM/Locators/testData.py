from OrangeHRM.Locators.locators import Locators
class TestData():
    #url
    login_url ="https://opensource-demo.orangehrmlive.com/"
    assign_leave_url = "https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave"

    #Login
    login_url = "https://opensource-demo.orangehrmlive.com/"
    logout_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    invalid_credential_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials"

    login_browser_title = "OrangeHRM"
    admin_username = "Admin"
    admin_password = "admin123"
    admin_username_invalid = "Admin1"
    admin_password_invalid = "admin123!"


    #Assign Leave

    leave_from_date = "2019-08-28"
    leave_to_date = "2019-08-28"
    leave_type_value = "1"
    text_strip1 = "view details"
    text_strip2 = "Balance not sufficient"


    emp_name = "Thomas Fleming"
    date11 = "2019-09-03"
    date12 = "2019-09-03"
    date21 = "2019-09-03"
    date22 = "2019-09-03"
    date31 = "2019-09-04"
    date32 = "2019-09-10"
    leave_type = Locators.leave_types_dropdown
    leave_type_value = "2"
    leave_comments = "Comments"

    #Entitlement
    add_entitlement= "https://opensource-demo.orangehrmlive.com/index.php/leave/addLeaveEntitlement"
    entitlement_emp_name = "Thomas Fleming"
    entitlement_type_option_value = "2"
    entitlement_period_option_value = "2019-01-01$$2019-12-31"
    entitlement_value = "2"
