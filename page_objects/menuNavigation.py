from selenium.webdriver.common.by import By


class MenuNavigation:

    def __init__(self, driver):
        self.driver = driver

    leave_menu_button = (By.ID, 'menu_leave_viewLeaveModule')
    configure_submenu_button = (By.ID, "menu_leave_Configure")
    leave_types_button = (By.ID, 'menu_leave_leaveTypeList')

    entitlements_submenu_button = (By.ID, "menu_leave_Entitlements")
    add_entitlement_button = (By.ID, 'menu_leave_addLeaveEntitlement')

    def getLeaveButton(self):
        return self.driver.find_element(*MenuNavigation.leave_menu_button)

    def getConfigureButton(self):
        return self.driver.find_element(*MenuNavigation.configure_submenu_button)

    def getLeaveTypesButton(self):
        return self.driver.find_element(*MenuNavigation.leave_types_button)

    def getEntitlementsButton(self):
        return self.driver.find_element(*MenuNavigation.entitlements_submenu_button)

    def getAddEntitlementButton(self):
        return self.driver.find_element(*MenuNavigation.add_entitlement_button)