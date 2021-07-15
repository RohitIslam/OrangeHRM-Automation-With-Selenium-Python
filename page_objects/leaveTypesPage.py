from selenium.webdriver.common.by import By


class LeaveTypesPage:

    def __init__(self, driver):
        self.driver = driver

    add_leaveType_button = (By.NAME, 'btnAdd')
    leaveType_name_field = (By.ID, 'leaveType_txtLeaveTypeName')
    isEntitlement_checkbox = (By.ID, 'leaveType_excludeIfNoEntitlement')
    leaveType_save_button = (By.NAME, 'saveButton')
    save_message = (By.CLASS_NAME, "message")

    def getAddLeaveTypeButton(self):
        return self.driver.find_element(*LeaveTypesPage.add_leaveType_button)

    def getLeaveTypeNameField(self):
        return self.driver.find_element(*LeaveTypesPage.leaveType_name_field)

    def getIsEntitlementCheckbox(self):
        return self.driver.find_element(*LeaveTypesPage.isEntitlement_checkbox)

    def getLeaveTypeSaveButton(self):
        return self.driver.find_element(*LeaveTypesPage.leaveType_save_button)

    def getSaveText(self):
        return self.driver.find_element(*LeaveTypesPage.save_message).text