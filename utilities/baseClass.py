import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("setup")
class BaseClass:

    # Select Element By Visible Text
    def selectOptionByText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    # Explicitly wait 5 secs for the element
    def verifyElementPresent(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(locator))
