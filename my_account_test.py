from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://automationpractice.com/index.php")


# selectors
login_selector = (By.CLASS_NAME, "login")
email_selector = (By.ID, "email")
password_selector = (By.ID, "passwd")
sign_in_button_selector = (By.ID, "SubmitLogin")

addresses_button_selector = (By.XPATH, "//a[@title='Addresses']")
credit_slips_button_selector = (By.XPATH, "//span[contains(text(),'My credit slips')]")
addresses_selector = (By.CSS_SELECTOR, ".bloc_adresses.row")
credit_slips_selector = (By.XPATH, "//p[contains(text(),'You have not received any credit slips.')]")

# actions/page navigation

## login
def test_login():
    driver.find_element(*login_selector).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(email_selector)).send_keys("seleniumwsh@gmail.com")
    driver.find_element(*password_selector).send_keys("test123")
    driver.find_element(*sign_in_button_selector).click()


## my account check
def test_addresses():
    driver.find_element(*addresses_button_selector).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(addresses_selector))
    driver.back()


def test_credit_slips():
    driver.find_element(*credit_slips_button_selector).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(credit_slips_selector))
    driver.quit()





