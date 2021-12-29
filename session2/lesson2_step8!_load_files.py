"""
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.
"""

import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим текстовое поле и вводим значение в текстовое поле
    input1 = browser.find_element_by_xpath('//input[@class="form-control" and @name="firstname" and @required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@class="form-control" and @name="lastname" and @required]')
    input2.send_keys("Popovych")
    input3 = browser.find_element_by_xpath('//input[@class="form-control" and @name="email" and @required]')
    input3.send_keys("ivan_popovych@gmail.com")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print("current_dir: ", os.path.abspath(os.path.dirname(__file__)))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    print("file_path: ", file_path)

    # загружаем файл
    choose_file = browser.find_element_by_xpath('//input[@id="file" and @type="file" and @required]')
    choose_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@class="btn btn-primary"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
