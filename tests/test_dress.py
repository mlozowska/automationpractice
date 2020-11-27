from pages.dress_page import DressPage
from pages.main_page import MainPage


def test_dress_results(driver):
    dress_page = DressPage(driver)
    main_page = MainPage(driver)
    main_page.search_dress()
    dress_page.dress()

