"""
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов.
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.

Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html.
Ваш код и для нее тоже должен пройти успешно.
"""

from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


def summa(values):
    return sum(values)

try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_xpath('//span[@id="num1"]')
    num1_ = int(num1.text)
    print(num1_)
    num2 = browser.find_element_by_xpath('//span[@id="num2"]')
    num2_ = int(num2.text)
    print(num2_)

    values = (num1_, num2_)
    summ = summa(values)
    print('summa=', summ)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))  # ищем элемент в списке, равный сумме

    button = browser.find_element_by_xpath('//button[@class="btn btn-default" and text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
