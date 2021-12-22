# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/registration1.html"
    # Метод get() сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)
    # browser.get("http://suninjuly.github.io/registration1.html")

    # Ваш код, который заполняет обязательные поля
    # input1 = browser.find_element_by_class_name("form-control.first")
    input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
    input1.send_keys("Ivan")
    # input2 = browser.find_element_by_class_name("form-control.second")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input2.send_keys("Popovych")
    # input3 = browser.find_element_by_class_name("form-control.third")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("ivan_popovych@gmail.com")

    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element(By.CLASS_NAME, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    # elements = browser.find_elements_by_tag_name("input[type=\"text\"]")
    elements = browser.find_element(By.TAG_NAME, "input[type=\"text\"]")
    print(elements)
    for element in elements:
        print(element)
        element.send_keys("Ivan")

    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
print(text)
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    # В качестве аргумента в метод find_element_by_link_text(text) передается такой текст, ссылку с которым мы хотим найти.
    # находим элемент по полному соответствию текста - Это тот самый текст,
    # который содержится между открывающим и закрывающим тегом <a> вот тут </a>
    link = browser.find_element(By.LINK_TEXT, text)
    # в link - ссылка по найденому текста
    time.sleep(5)
    # кликаем по найденной ссылке
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Popovych")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Lviv")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Ukraine")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')

    input1 = browser.find_element(By.XPATH, '//input[@id="answer" and @class="form-control" and @required]')
    # загружаем файл
    input1.send_keys(file_path)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
