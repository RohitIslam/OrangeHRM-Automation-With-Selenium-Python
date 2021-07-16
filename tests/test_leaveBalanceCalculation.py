import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from page_objects.leaveEntitlementsPage import LeaveEntitlementsPage
from page_objects.menuNavigation import MenuNavigation
from page_objects.leaveTypesPage import LeaveTypesPage
from page_objects.loginPage import LoginPage
from utilities.baseClass import BaseClass


class TestLeaveBalanceCalculation(BaseClass):
    def test_leave_balance_calculation(self):
        action = ActionChains(self.driver)

        loginPage = LoginPage(self.driver)
        menuNavigation = MenuNavigation(self.driver)
        leaveTypesPage = LeaveTypesPage(self.driver)
        leaveEntitlementsPage = LeaveEntitlementsPage(self.driver)

        # Login as Admin
        admin_username = 'Admin'
        admin_pass = 'admin123'

        loginPage.getUsernameField().send_keys(admin_username)
        loginPage.getPassField().send_keys(admin_pass)
        loginPage.getLoginButton().click()

        # Creating Leave type
        leave_type = 'BD - EID'

        action = ActionChains(self.driver)
        action.move_to_element(menuNavigation.getLeaveButton()).perform()
        action.move_to_element(menuNavigation.getConfigureButton()).perform()
        action.move_to_element(menuNavigation.getLeaveTypesButton()).click().perform()

        leaveTypesPage.getAddLeaveTypeButton().click()
        leaveTypesPage.getLeaveTypeNameField().send_keys(leave_type)
        leaveTypesPage.getIsEntitlementCheckbox().click()
        leaveTypesPage.getLeaveTypeSaveButton().click()

        assert leaveTypesPage.getSaveText() == "Successfully Saved", "Save message did not matched."
        self.driver.refresh()

        # Adding Leave Entitlements
        entitlement_days = 30

        action = ActionChains(self.driver)
        action.move_to_element(menuNavigation.getEntitlementsButton()).perform()
        action.move_to_element(menuNavigation.getAddEntitlementButton()).click().perform()

        leaveEntitlementsPage.getMultipleEmployeesCheckbox().click()
        self.selectByText(leaveEntitlementsPage.getLeaveTypeDropdown(), leave_type)
        leaveEntitlementsPage.getEntitlementField().send_keys(entitlement_days)

        time.sleep(2)
        leaveEntitlementsPage.getEntitlementSaveButton().click()
