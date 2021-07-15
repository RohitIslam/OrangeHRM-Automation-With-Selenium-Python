from selenium.webdriver import ActionChains

from page_objects.dashboardPage import DashboardPage
from page_objects.loginPage import LoginPage
from utilities.baseClass import BaseClass


class TestLeaveBalanceCalculation(BaseClass):
    def test_leave_balance_calculation(self):
        action = ActionChains(self.driver)

        loginPage = LoginPage(self.driver)
        dashboardPage = DashboardPage(self.driver)

        # Login as Admin
        admin_username = 'Admin'
        admin_pass = 'admin123'

        loginPage.getUsernameField().send_keys(admin_username)
        loginPage.getPassField().send_keys(admin_pass)
        loginPage.getLoginButton().click()

        # Creating Leave type
        action.move_to_element(dashboardPage.getLeaveButton()).perform()
        action.move_to_element(dashboardPage.getConfigureButton()).perform()
        action.move_to_element(dashboardPage.getLeaveTypesButton()).click().perform()