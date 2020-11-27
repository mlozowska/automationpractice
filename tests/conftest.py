import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get("http://automationpractice.com/index.php")

    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)
    return driver
