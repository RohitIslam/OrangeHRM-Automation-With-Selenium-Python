from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    leave_menu_button = (By.ID, 'menu_leave_viewLeaveModule')
    configure_submenu_button = (By.ID, "menu_leave_Configure")
    leave_types_button = (By.ID, 'menu_leave_leaveTypeList')

    def getLeaveButton(self):
        return self.driver.find_element(*DashboardPage.leave_menu_button)

    def getConfigureButton(self):
        return self.driver.find_element(*DashboardPage.configure_submenu_button)

    def getLeaveTypesButton(self):
        return self.driver.find_element(*DashboardPage.leave_types_button)