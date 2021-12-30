# Run file from Terminal using command:
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3/lesson2$ python3 lesson2_step13!_unittest_my.py

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest


class TestRegistrationOnSite(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        input2.send_keys("Popovych")
        input3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        input3.send_keys("ivan_popovych@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "(test_registration1): Registration Failed!")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        input2.send_keys("Popovych")
        input3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        input3.send_keys("ivan_popovych@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "(test_registration2): Registration Failed!")


if __name__ == "__main__":
    unittest.main()
