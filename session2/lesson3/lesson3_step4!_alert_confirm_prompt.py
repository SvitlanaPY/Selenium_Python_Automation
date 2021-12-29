"""
Задание: принимаем alert

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом.
Отправьте полученное число в качестве ответа на это задание.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# вычисляем 'x'
def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/alert_accept.html"
    # Метод get() сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    # Нажимаем на кнопку "I want to go on a magical journey!"
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    button.click()

    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # ищим число "х" и записываем в переменную "num1_" текст из элемента "num1"
    num1 = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    num1_ = int(num1.text)
    print(num1_)

    # вычисляем "calc_num1_" по формуле вызывая функцию "calc()"
    calc_num1_ = calc(num1_)
    print("calc_num1_= ", calc_num1_)

    # находим текстовое поле и вводим значение 'calc_num1_' в текстовое поле
    input1 = browser.find_element(By.XPATH, '//input[@class="form-control" and @id="answer" and @required]')
    input1.send_keys(calc_num1_)

    # Нажимаем на кнопку "submit"
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary" and @type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
