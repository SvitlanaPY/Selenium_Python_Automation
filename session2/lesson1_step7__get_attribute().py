"""
Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной 'х' спрятано в "сундуке",
точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:
Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом.
Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
"""

from selenium import webdriver
import time
import math

# вычисляем 'x'
def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sunduk_image = browser.find_element_by_id("treasure")
    img_valuex = sunduk_image.get_attribute("valuex")
    print("value of image valuex: ", img_valuex, type(img_valuex))
    # value of image valuex:  188 <class 'str'>

    value_x = calc(img_valuex)
    print("value_x= ", value_x)

    # вводим значение 'value_x' в текстовое поле
    input1 = browser.find_element_by_xpath('//input[@id="answer" and @required]')
    input1.send_keys(value_x)

    # отмечаем checkbox "I'm the robot":
    option_checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox" and @required]')
    option_checkbox.click()

    # выбираем radiobutton "Robots rule!":
    option_radiobutton = browser.find_element_by_xpath('//input[@id="robotsRule" and @value="robots"]')
    option_radiobutton.click()

    # отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@class="btn btn-default"  and text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
