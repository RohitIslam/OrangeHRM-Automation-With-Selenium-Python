from selenium.webdriver import ActionChains

from page_objects.dashboardPage import DashboardPage
from page_objects.leaveTypesPage import LeaveTypesPage
from page_objects.loginPage import LoginPage
from utilities.baseClass import BaseClass


class TestLeaveBalanceCalculation(BaseClass):
    def test_leave_balance_calculation(self):
        action = ActionChains(self.driver)

        loginPage = LoginPage(self.driver)
        dashboardPage = DashboardPage(self.driver)
        leaveTypesPage = LeaveTypesPage(self.driver)

        # Login as Admin
        admin_username = 'Admin'
        admin_pass = 'admin123'

        loginPage.getUsernameField().send_keys(admin_username)
        loginPage.getPassField().send_keys(admin_pass)
        loginPage.getLoginButton().click()

        # Creating Leave type
        leave_type = 'AB - CD'
        action.move_to_element(dashboardPage.getLeaveButton()).perform()
        action.move_to_element(dashboardPage.getConfigureButton()).perform()
        action.move_to_element(dashboardPage.getLeaveTypesButton()).click().perform()

        leaveTypesPage.getAddLeaveTypeButton().click()
        leaveTypesPage.getLeaveTypeNameField().send_keys(leave_type)
        leaveTypesPage.getIsEntitlementCheckbox().click()
        leaveTypesPage.getLeaveTypeSaveButton().click()

        # leaveType_save_text = leaveTypesPage.getSaveText().text

        assert leaveTypesPage.getSaveText() == "Successfully Saved", "Save message did not matched."
