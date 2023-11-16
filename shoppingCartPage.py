from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from pages_.basePage import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.remove_buttons_locator = (By.CSS_SELECTOR, "[value='Delete']")
        self.delete_button_locator = (By.XPATH, "//button[@class='delete-button']")

    def delete_all_from_cart(self):
        remove_buttons = self.driver.find_elements(self.remove_buttons_locator)
        for remove_button in remove_buttons:
            self.click_and_wait(remove_button)

    def delete_from_cart(self):
        delete_button = self.driver.find_element(self.delete_button_locator)
        self.click_and_wait(delete_button)

    def click_and_wait(self, element):
        element.click()
        try:
            WebDriverWait(self.driver, 10).until(EC.staleness_of(element))
        except StaleElementReferenceException:
            pass
