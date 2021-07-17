from selenium.webdriver.common.by import By


class LeaveListPage:

    def __init__(self, driver):
        self.driver = driver

    result_table = (By.XPATH, "//table[@id='resultTable']/tbody")
    result_table_rows = (By.XPATH, "//table[@id='resultTable']/tbody/tr")
    result_table_cols = (By.TAG_NAME, "td")
    leave_approve_save_button = (By.ID, 'btnSave')
    leave_approve_save_message = (By.CLASS_NAME, "message")

    def getResultTable(self):
        return self.driver.find_element(*LeaveListPage.result_table)

    def getResultTableRows(self):
        return self.driver.find_elements(*LeaveListPage.result_table_rows)

    def getResultTableCols(self):
        return self.driver.find_elements(*LeaveListPage.result_table_cols)

    def getLeaveApproveSaveButton(self):
        return self.driver.find_element(*LeaveListPage.leave_approve_save_button)

    def getApproveDropdown(self):
        rows = self.driver.find_elements(*LeaveListPage.result_table_rows)
        for i in range(len(rows)):
            columns = rows[i].find_elements(*LeaveListPage.result_table_cols)
            for j in range(len(columns)):
                if columns[j].text == "Alvi Tazwar":
                    return columns[7].find_element(By.TAG_NAME, 'select')

    def getApproveSaveText(self):
        return self.driver.find_element(*LeaveListPage.leave_approve_save_message).text
