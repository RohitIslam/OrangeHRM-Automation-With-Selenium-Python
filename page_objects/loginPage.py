from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_field = (By.ID, "txtUsername")
    password_field = (By.ID, "txtPassword")
    login_button = (By.ID, "btnLogin")

    def getUsernameField(self):
        # '*' deserializes the Tuple.
        return self.driver.find_element(*LoginPage.username_field)

    def getPassField(self):
        return self.driver.find_element(*LoginPage.password_field)

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.login_button)
