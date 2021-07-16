from selenium.webdriver.common.by import By


class LeaveEntitlementsPage:

    def __init__(self, driver):
        self.driver = driver

    multiple_employees_checkbox = (By.ID, 'entitlements_filters_bulk_assign')
    employee_match_text_locator = (By.XPATH, "//span[@id='ajax_count']")
    employee_list_table = (By.CLASS_NAME, 'table')
    leave_type_dropdown = (By.ID, 'entitlements_leave_type')
    entitlement_field = (By.ID, 'entitlements_entitlement')
    entitlement_save_button = (By.ID, 'btnSave')
    save_message = (By.CLASS_NAME, 'message')
    entitlement_confirm_button = (By.XPATH, "//input[@id='dialogConfirmBtn']")

    def getMultipleEmployeesCheckbox(self):
        return self.driver.find_element(*LeaveEntitlementsPage.multiple_employees_checkbox)

    def getLeaveTypeDropdown(self):
        return self.driver.find_element(*LeaveEntitlementsPage.leave_type_dropdown)

    def getEntitlementField(self):
        return self.driver.find_element(*LeaveEntitlementsPage.entitlement_field)

    def getEntitlementSaveButton(self):
        return self.driver.find_element(*LeaveEntitlementsPage.entitlement_save_button)

    def getEntitlementSaveText(self):
        return self.driver.find_element(*LeaveEntitlementsPage.save_message).text

    def getEntitlementConfirmButton(self):
        return self.driver.find_element(*LeaveEntitlementsPage.entitlement_confirm_button)