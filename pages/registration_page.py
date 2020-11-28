from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    new_email_selector = (By.ID, "email_create")
    create_account_selector = (By.ID, "SubmitCreate")

    def registration(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.new_email_selector)).send_keys(
            "xyz20202@gmail.com")
        self.driver.find_element(*self.create_account_selector).click()