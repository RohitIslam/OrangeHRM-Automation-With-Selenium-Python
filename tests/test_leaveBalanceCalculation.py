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

        assert leaveTypesPage.getLeaveTypeSaveText() == "Successfully Saved", "Save message did not matched."

        # Adding Leave Entitlements
        entitlement_days = 30

        action = ActionChains(self.driver)
        action.move_to_element(menuNavigation.getEntitlementsButton()).perform()
        action.move_to_element(menuNavigation.getAddEntitlementButton()).click().perform()

        leaveEntitlementsPage.getMultipleEmployeesCheckbox().click()
        self.verifyElementPresent(leaveEntitlementsPage.employee_match_text_locator)
        self.selectOptionByText(leaveEntitlementsPage.getLeaveTypeDropdown(), leave_type)
        leaveEntitlementsPage.getEntitlementField().send_keys(entitlement_days)
        leaveEntitlementsPage.getEntitlementSaveButton().click()

        # Handling Employee List Modal
        self.verifyElementPresent(leaveEntitlementsPage.employee_list_table)
        self.verifyElementPresent(leaveEntitlementsPage.entitlement_confirm_button)
        leaveEntitlementsPage.getEntitlementConfirmButton().click()
        self.verifyElementPresent(leaveEntitlementsPage.save_message)

        assert leaveEntitlementsPage.getEntitlementSaveText() == "Entitlements added to 40 employees(s)", \
            "Save message did not matched."

        # Login as Employee and apply for the 5days
