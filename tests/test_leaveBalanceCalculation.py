from page_objects.loginPage import LoginPage
from utilities.baseClass import BaseClass


class TestLeaveBalanceCalculation(BaseClass):
    def test_leave_balance_calculation(self):
        loginPage = LoginPage(self.driver)

        # Login as Admin
        admin_username = 'Admin'
        admin_pass = 'admin123'

        loginPage.getUsernameField().send_keys(admin_username)
        loginPage.getPassField().send_keys(admin_pass)
        loginPage.getLoginButton().click()