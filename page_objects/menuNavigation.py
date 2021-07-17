from selenium.webdriver.common.by import By


class MenuNavigation:

    def __init__(self, driver):
        self.driver = driver

    welcome_user_button = (By.ID, 'welcome')
    logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")

    dashboard_menu_button = (By.ID, 'menu_dashboard_index')

    leave_menu_button = (By.ID, 'menu_leave_viewLeaveModule')
    applyLeave_submenu_button = (By.ID, 'menu_leave_applyLeave')
    configure_submenu_button = (By.ID, "menu_leave_Configure")
    leave_types_button = (By.ID, 'menu_leave_leaveTypeList')
    leaveList_submenu_button = (By.ID, 'menu_leave_viewLeaveList')

    entitlements_submenu_button = (By.ID, "menu_leave_Entitlements")
    add_entitlement_button = (By.ID, 'menu_leave_addLeaveEntitlement')

    def getWelcomeButton(self):
        return self.driver.find_element(*MenuNavigation.welcome_user_button)

    def getLogoutButton(self):
        return self.driver.find_element(*MenuNavigation.logout_button)

    def getDashboardButton(self):
        return self.driver.find_element(*MenuNavigation.dashboard_menu_button)

    def getLeaveButton(self):
        return self.driver.find_element(*MenuNavigation.leave_menu_button)

    def getApplyLeaveButton(self):
        return self.driver.find_element(*MenuNavigation.applyLeave_submenu_button)

    def getConfigureButton(self):
        return self.driver.find_element(*MenuNavigation.configure_submenu_button)

    def getLeaveTypesButton(self):
        return self.driver.find_element(*MenuNavigation.leave_types_button)

    def getLeaveListButton(self):
        return self.driver.find_element(*MenuNavigation.leaveList_submenu_button)

    def getEntitlementsButton(self):
        return self.driver.find_element(*MenuNavigation.entitlements_submenu_button)

    def getAddEntitlementButton(self):
        return self.driver.find_element(*MenuNavigation.add_entitlement_button)