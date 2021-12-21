"""
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке,
нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом.
Отправьте полученное число в качестве ответа на это задание.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# вычисляем 'calc_num1_'
def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/redirect_accept.html"
    # Метод get() сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    # Нажимаем на кнопку "I want to go on a magical journey!"
    button = browser.find_element_by_xpath('//button[@class="trollface btn btn-primary"]')
    button.click()

    # узнаем имя новой вкладки
    window_name = browser.window_handles[1]

    # переключаемся на новую вкладку
    browser.switch_to.window(window_name)

    # ищим число "х" и записываем в переменную "num1_" текст из элемента "num1"
    num1 = browser.find_element_by_xpath('//span[@id="input_value"]')
    num1_ = int(num1.text)
    print(num1_)

    # вычисляем "calc_num1_" по формуле вызывая функцию "calc()"
    calc_num1_ = calc(num1_)
    print("calc_num1_= ", calc_num1_)

    # находим текстовое поле и вводим значение 'calc_num1_' в текстовое поле
    input1 = browser.find_element_by_xpath('//input[@class="form-control" and @id="answer" and @required]')
    input1.send_keys(calc_num1_)

    # Нажимаем на кнопку "submit"
    button = browser.find_element_by_xpath('//button[@class="btn btn-primary" and @type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
