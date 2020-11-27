from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://automationpractice.com/index.php")

driver.find_element_by_id("header_logo")
driver.find_element_by_class_name("shopping_cart")
driver.find_element_by_id("newsletter-input")
driver.find_element_by_class_name("twitter")
driver.find_element_by_class_name("homefeatured")
driver.find_element_by_id("contact-link")

# CSS selectors
driver.find_element_by_css_selector(".logo")
driver.find_element_by_css_selector(".shopping_cart")
driver.find_element_by_css_selector("#newsletter-input")
driver.find_element_by_css_selector(".twitter")
driver.find_element_by_css_selector(".homefeatured")
driver.find_element_by_css_selector("#contact-link")

# xpath selectors
driver.find_element_by_xpath("//div[@class='shopping_cart']")
driver.find_element_by_xpath("//div[@class='shopping_cart']")
driver.find_element_by_xpath("//input[@id='newsletter-input']")
driver.find_element_by_xpath("//li[@class='twitter']")
driver.find_element_by_xpath("//*[@class='homefeatured']")
driver.find_element_by_xpath("//*[@title='Contact Us']")

driver.quit()

