import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def link_check(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Введите имя"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Введите фамилию"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Введите Email"]')
    input3.send_keys("ivanpetrov@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text


class TestLinks(unittest.TestCase):
    def test_link1(self):
        welcome_text = link_check("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_link2(self):
        welcome_text = link_check("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)


if __name__ == "__main__":
    unittest.main()

