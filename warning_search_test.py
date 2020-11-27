from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://automationpractice.com/index.php")

search_box_selector = (By.ID, "search_query_top")
submit_search_selector = (By.NAME, "submit_search")
warning_box_selector = (By.CSS_SELECTOR, ".alert.alert-warning")

def test_warning_box():
    driver.find_element(*search_box_selector).send_keys("test")
    driver.find_element(*submit_search_selector).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(warning_box_selector))
    driver.quit()


