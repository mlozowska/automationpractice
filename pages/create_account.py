from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NewAccountPage(BasePage):

    mrs_selector = (By.ID, "id_gender2")
    first_name_selector = (By.CSS_SELECTOR, "#customer_firstname")
    last_name_selector = (By.ID, "customer_lastname")
    password_selector = (By.ID, "passwd")
    address_selector = (By.CSS_SELECTOR, "#address1")
    city_selector = (By.NAME, "city")
    state_selector = (By.CSS_SELECTOR, "#id_state")
    exact_state_selector = (By.XPATH, "//option[contains(text(),'California')]")
    zip_code_selector = (By.ID, "postcode")
    country_selector = (By.ID, "uniform-id_country")
    exact_country_selector = (By.XPATH, "//option[contains(text(),'United States')]")
    phone_selector = (By.CSS_SELECTOR, "#phone_mobile")
    alias_selector = (By.CSS_SELECTOR, ".form-control")
    button_register_selector = (By.NAME, "submitAccount")

    def create_account(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.mrs_selector)).click()
        self.driver.find_element(*self.first_name_selector).send_keys("Izolda")
        self.driver.find_element(*self.last_name_selector).send_keys("MacGyver")
        self.driver.find_element(*self.password_selector).send_keys("test12345")
        self.driver.find_element(*self.address_selector).send_keys("Abbey Road 3")
        self.driver.find_element(*self.city_selector).send_keys("Vladivostok")

        self.driver.find_element(*self.state_selector).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.exact_state_selector)).click()

        self.driver.find_element(*self.zip_code_selector).send_keys("00300")
        time.sleep(3)
        self.driver.find_element(*self.country_selector).click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.exact_country_selector)).click()
        self.driver.find_element(*self.phone_selector).send_keys("7543010")

        self.driver.find_element(*self.alias_selector).send_keys("Abbey Road 3,P.O. Box, Utest")
        self.driver.find_element(*self.button_register_selector).click()






