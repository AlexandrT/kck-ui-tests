from selenium.webdriver.common.by import By


class SigninPageLocators(object):
    LOGIN_INPUT = (By.ID, 'UserLogin_username')
    PASSWORD_INPUT = (By.ID, 'UserLogin_password')

    SIGNIN_BUTTON = (By.XPATH, '//input[@class="btn btn-info col-sm-4 logbu"]')

    PROFILE_BUTTON = (By.XPATH, '//button[contains(@class, "profile-nav-btn")]')

    LOGIN_ERROR = (By.XPATH, '//input[@id="UserLogin_username"]/following-sibling::small')
    PASSWORD_ERROR = (By.XPATH, '//input[@id="UserLogin_password"]/following-sibling::small')
