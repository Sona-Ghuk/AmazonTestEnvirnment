from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = None
        self.search_page = None

    def search_product(self, query):
        self.send_keys_to_element(By.ID, "twotabsearchtextbox", query)
        self.send_keys_to_element(By.ID, "twotabsearchtextbox", Keys.RETURN)

    def test_search_and_filter(self):
        self.login_page.login("sona.ghukasyan@gmail.com", "hasiko07")
        self.search_page.search_product("adidas shoes women")

    def send_keys_to_element(self, ID, param, query):
        pass
