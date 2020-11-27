from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    login_selector = (By.CLASS_NAME, "login")
    search_box_selector = (By.ID, "search_query_top")
    submit_search_selector = (By.NAME, "submit_search")

    def go_to_login(self):
        self.driver.find_element(*self.login_selector).click()

    def search_dress(self):
        self.driver.find_element(*self.search_box_selector).send_keys("dress")
        self.driver.find_element(*self.submit_search_selector).click()
