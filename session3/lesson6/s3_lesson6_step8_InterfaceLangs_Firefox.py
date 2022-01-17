from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
