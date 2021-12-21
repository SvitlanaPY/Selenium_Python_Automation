"""
Работа со списками
На веб-страницах мы также встречаем раскрывающиеся (выпадающие) списки.
У таких списков есть несколько важных особенностей:
У каждого элемента списка обычно есть уникальное значение атрибута value
В списках может быть разрешено выбирать как только один, так и несколько вариантов, в зависимости от типа списка
Визуально списки могут различаться тем, что в одном случае все варианты скрыты в выпадающем меню
(http://suninjuly.github.io/selects1.html),
а в другом все варианты или их часть видны
(http://suninjuly.github.io/selects2.html)
Но для взаимодействия с любым вариантом списка мы будем использовать одни и те же методы Selenium.

Посмотрим, как выглядит html для списка:
<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
<option selected>--</option>
<option value="1">Python</option>
<option value="2">Java</option>
<option value="3">JavaScript</option>
</select>
Варианты ответа задаются тегом option, значение value может отсутствовать.
Можно отмечать варианты с помощью обычного метода click().

Для этого сначала нужно применить метод click() для элемента с тегом select, чтобы список раскрылся,
а затем кликнуть на нужный вариант ответа:
from selenium import webdriver
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()

Последняя строчка может выглядеть и так:
browser.find_element_by_css_selector("[value='1']").click()

Это не самый удобный способ, так как нам приходится делать лишний клик для открытия списка.
Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver.
Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select.
Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
Первый способ ищет элемент по видимому тексту,
например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру.
Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python",
нужно использовать select.select_by_index(1),
так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".
"""

from selenium import webdriver
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

    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("option:nth-child(2)").click()
    # Или так:
    # browser.find_element_by_css_selector("[value='1']").click()

    button = browser.find_element_by_xpath('//button[@class="btn btn-default" and text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
