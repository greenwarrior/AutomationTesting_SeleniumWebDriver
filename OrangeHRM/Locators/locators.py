class Locators():
    # Login page objects
    username_textbox_id = "txtUsername"
    password_textbox_id = "txtPassword"
    login_button_id = "btnLogin"
    invalidUsername_span_xpath = "//*[@id='spanMessage']"
    invalidUsername_span_message = "[contains(text(),'Invalid credentials')]"



    # Home page objects
    welcome_link_id = "welcome"
    logout_link_linkText = "Logout"

    #Assign Leave
    assign_leave_view_leave_module_menu_id = "menu_leave_viewLeaveModule"
    leave_assign_leave_link = "menu_leave_assignLeave"
    employee_name_textbox_id = "assignleave_txtEmployee_empName"
    leave_types_dropdown = "assignleave_txtLeaveType"
    leave_type_dropdown_options = "option"
    leave_from_date_datepicker = "assignleave_txtFromDate"
    leave_to_date_datepicker  = "assignleave_txtToDate"
    leave_comment_textarea   = "assignleave_txtComment"
    leave_assign_button     = "assignBtn"
    leave_confirm_leave_button = "confirmOkButton"
    assign_leave_balance_label = "assignleave_leaveBalance"

    # Add employee entitlement
    entitlement_menu_id = "menu_leave_Entitlements"
    entitlement_leave_menu_id = "menu_leave_addLeaveEntitlement"
    entitlement_leave_empname_input_id= "entitlements_employee_empName"
    entitlement_type_dropdown_id= "entitlements_leave_type"
    entitlement_type_option_tagname = "option"
    entitlement_period_dropdown = "period"
    entitlement_period_option_tagname = "option"
    entitlement__days_input_xpath = "//*[@id='frmLeaveEntitlementAdd']/fieldset/ol/li[5]/input[1]"
    entitlement_save_button_id = "btnSave"
    entitlement_update_confirm_button_id = "dialogUpdateEntitlementConfirmBtn"
    entitlement_update_cancel_button_id = "dialogUpdateEntitlementCancelBtn"
    entitlement_search_button_id = "#searchBtn"


