from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.create_account import NewAccountPage


def test_create_account(driver):
    create_account_page = NewAccountPage(driver)
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)
    main_page.go_to_login()
    registration_page.registration()
    create_account_page.create_account()