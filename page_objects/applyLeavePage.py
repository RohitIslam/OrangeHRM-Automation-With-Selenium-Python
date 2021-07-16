from selenium.webdriver.common.by import By


class ApplyLeavePage:

    def __init__(self, driver):
        self.driver = driver

    from_date = '16'
    to_date = '22'

    apply_leave_type_dropdown = (By.ID, 'applyleave_txtLeaveType')
    apply_leave_from_date_field = (By.ID, 'applyleave_txtFromDate')
    apply_leave_from_date_picker = (By.XPATH, f"//a[contains(text(),{from_date})]")
    apply_leave_to_date_field = (By.ID, 'applyleave_txtToDate')
    apply_leave_to_date_picker = (By.XPATH, f"//a[contains(text(),{to_date})]")
    apply_button = (By.ID, 'applyBtn')
    leave_balance_left = (By.ID, 'applyleave_leaveBalance')

    def getApplyLeaveTypeDropdown(self):
        return self.driver.find_element(*ApplyLeavePage.apply_leave_type_dropdown)

    def getApplyLeaveFromDateField(self):
        return self.driver.find_element(*ApplyLeavePage.apply_leave_from_date_field)

    def getApplyLeaveFromDatePicker(self):
        return self.driver.find_element(*ApplyLeavePage.apply_leave_from_date_picker)

    def getApplyLeaveToDateField(self):
        return self.driver.find_element(*ApplyLeavePage.apply_leave_to_date_field)

    def getApplyLeaveToDatePicker(self):
        return self.driver.find_element(*ApplyLeavePage.apply_leave_to_date_picker)

    def getApplyButton(self):
        return self.driver.find_element(*ApplyLeavePage.apply_button)

    def getLeaveBalanceLeftText(self):
        return self.driver.find_element(*ApplyLeavePage.leave_balance_left).text
