import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    # Select Element By Visible Text
    def selectByText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)
