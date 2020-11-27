# search 'dress', verify if any item is found
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DressPage(BasePage):

    dress_number_selector = (By.CSS_SELECTOR, ".heading-counter")
    dress_results_selector = (By.XPATH, "//div[@class='product-container']")


    def dress(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dress_results_selector))
        # added: show how many items have been found: '7 results have been found.'
        self.driver.find_element(*self.dress_number_selector)

