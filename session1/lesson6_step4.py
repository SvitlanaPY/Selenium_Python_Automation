"""
Задание: поиск элементов с помощью Selenium
Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium.
Если всё сделано правильно, то вы увидите окно с проверочным кодом.
Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено.
Однако благодаря Selenium вы сможете выполнить задачу до того, как время истечёт.

Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно только подставить нужные значения
для поиска вместо слов value1, value2 и т.д.
Обратите внимание, что значения нужно заключать в кавычки, т.к. они должны передаваться в виде строки.

from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
Системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет,
то последняя строчка, содержащая код, может не выполниться.

Создайте файл lesson6_step4.py (обратите внимание на расширение .py) и вставьте туда шаблон кода.
Подберите селекторы и запустите из командной строки, так же, как в уроке 2:

python lesson6_step4.py

Все последующие задачи с кодом запускайте по аналогии.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Popovych")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Lviv")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
