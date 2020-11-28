from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


def test_registration(driver):
    registration_page = RegistrationPage(driver)
    main_page = MainPage(driver)
    main_page.go_to_login()
    registration_page.registration()

