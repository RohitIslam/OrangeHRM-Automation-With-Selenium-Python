from selenium.webdriver.common.by import By


class LeaveEntitlementsPage:

    def __init__(self, driver):
        self.driver = driver

    multiple_employees_checkbox = (By.ID, 'entitlements_filters_bulk_assign')
    leave_type_dropdown = (By.ID, 'entitlements_leave_type')
    entitlement_field = (By.ID, 'entitlements_entitlement')
    entitlement_save_button = (By.ID, 'btnSave')

    def getMultipleEmployeesCheckbox(self):
        return self.driver.find_element(*LeaveEntitlementsPage.multiple_employees_checkbox)

    def getLeaveTypeDropdown(self):
        return self.driver.find_element(*LeaveEntitlementsPage.leave_type_dropdown)

    def getEntitlementField(self):
        return self.driver.find_element(*LeaveEntitlementsPage.entitlement_field)

    def getEntitlementSaveButton(self):
        return self.driver.find_element(*LeaveEntitlementsPage.entitlement_save_button)