import pytest
from selenium import webdriver
from pyvirtualdisplay import Display

from lib.config import settings

@pytest.fixture
def selenium(selenium, main_url):
    display = Display(visible=False, size=(1500, 1100))
    display.start()
    selenium.set_window_size(1400, 1000)
    selenium.implicitly_wait(2)
    return selenium

@pytest.fixture
def main_url():
    return settings.DOMAIN

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    return chrome_options
