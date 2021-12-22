"""
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач.
На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера,
но сложным для человека.
------------------------------------------------------------
Ваша программа должна выполнить следующие шаги:
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
Для этой задачи вам понадобится использовать атрибут .text для найденного элемента.
Обратите внимание, что скобки здесь не нужны:

x_element = browser.find_element_by_*(selector)
x = x_element.text
y = calc(x)
Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
Например, text для данного элемента
<div class="message">У вас новое сообщение.</div>
вернёт строку: "У вас новое сообщение".

Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле.
Не забудьте добавить этот код в начало вашего скрипта:

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом.
Скопируйте его в поле ниже.
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


# вычисляем 'x'
def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


try:

    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/math.html"
    # Метод get() сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    # находим элемент, содержащий значение для переменной 'x'
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    print(x_element)

    # записываем в переменную 'x' текст из элемента x_element
    x = x_element.text
    print("x= ", x)

    # записываем результат вычисления 'x'-а в переменную 'y'
    y = calc(x)
    print("y= ", y)

    # вводим значение 'y' в текстовое поле
    input1 = browser.find_element(By.XPATH, '//input[@id="answer" and @class="form-control" and @required]')
    input1.send_keys(y)

    # отмечаем checkbox "I'm the robot":
    option_checkbox = browser.find_element(By.XPATH, '//input[@id="robotCheckbox" and @class="form-check-input" and @required]')
    option_checkbox.click()

    # выбираем radiobutton "Robots rule!":
    option_radiobutton = browser.find_element(By.XPATH, '//label[@class="form-check-label" and text()="Robots rule"]')
    option_radiobutton.click()

    # отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-default"  and text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
