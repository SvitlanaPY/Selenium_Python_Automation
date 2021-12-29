"""
Задание: ждем нужный текст на странице

Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение.

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element
из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом.
Отправьте его в качестве ответа на это задание.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# вычисляем 'x'
def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
    # Открыть страницу по URL.
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    # Найти и нажать на кнопку "Book"
    button = browser.find_element(By.XPATH, '//button[@id="book" and text()="Book"]')
    # button = browser.find_element(By.ID, "book")
    button.click()

    # ищем элемент "х"
    num1 = browser.find_element(By.XPATH, '//span[@id="input_value"]')

    # записываем в переменную "num1_" значение/текст найденного "х"
    num1_ = int(num1.text)
    print(num1_)

    # вычисляем "calc_num1_" по формуле вызывая функцию "calc()"
    calc_num1_ = calc(num1_)
    print("calc_num1_= ", calc_num1_)

    # находим текстовое поле и вводим значение 'calc_num1_' в текстовое поле
    input1 = browser.find_element(By.XPATH, '//input[@class="form-control" and @id="answer" and @required]')
    input1.send_keys(calc_num1_)

    # Нажимаем на кнопку "submit"
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary" and @id="solve" and @type="submit"]')
    # button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
