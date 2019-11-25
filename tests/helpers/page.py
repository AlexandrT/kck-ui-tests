from selenium.common.exceptions import NoSuchElementException

from .locators import *
from .elements import *


class Login(SigninPageElement):
    locator = SigninPageLocators.LOGIN_INPUT

class Password(SigninPageElement):
    locator = SigninPageLocators.PASSWORD_INPUT

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_profile_btn_existed(self):
        try:
            element = self.driver.find_element(*SigninPageLocators.PROFILE_BUTTON)
            return True
        except NoSuchElementException:
            return False

class SigninPage(BasePage):
    login = Login()
    password = Password()

    def click_signin_btn(self):
        element = self.driver.find_element(*SigninPageLocators.SIGNIN_BUTTON)
        element.click()

    def get_login_error(self):
        element = self.driver.find_element(*SigninPageLocators.LOGIN_ERROR)
        return element.text

    def get_password_error(self):
        element = self.driver.find_element(*SigninPageLocators.PASSWORD_ERROR)
        return element.text
