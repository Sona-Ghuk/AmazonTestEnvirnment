import time
from telnetlib import EC

from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button_locator = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(self.add_to_cart_button_locator)
        add_to_cart_button.click()
        time.sleep(5)

    def delete_all_from_cart(self):
        remove_buttons = self.driver.find_elements(self.remove_buttons_locator)
        for remove_button in remove_buttons:
            remove_button.click()
            WebDriverWait(self.driver, 10).until(EC.staleness_of(remove_button))
