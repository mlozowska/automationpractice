from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    mrs_selector = (By.ID, "id_gender2")
    first_name_selector = (By.ID, "customer_firstname")
    last_name_selector = (By.ID, "customer_lastname")
    password_selector = (By.ID, "passwd")
    birth_day_selector = (By.ID, "days")
    birth_month_selector = (By.ID, "months")
    birth_year_selector = (By.ID, "years")



