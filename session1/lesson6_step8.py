"""
Задание: поиск элемента по XPath
На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
при этом в нее добавилась куча одинаковых кнопок отправки.
Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё.

Ваши шаги:
В коде из шага 4 замените ссылку на http://suninjuly.github.io/find_xpath_form.
Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
Запустите ваш код.
Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код,
который нужно отправить в качестве ответа на это задание.
"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

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
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

