import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# список всех возможных ссылок/url
# url_id = [
#     'https://stepik.org/lesson/236895/step/1',
#     'https://stepik.org/lesson/236896/step/1',
#     'https://stepik.org/lesson/236897/step/1',
#     'https://stepik.org/lesson/236898/step/1',
#     'https://stepik.org/lesson/236899/step/1',
#     'https://stepik.org/lesson/236903/step/1',
#     'https://stepik.org/lesson/236904/step/1',
#     'https://stepik.org/lesson/236905/step/1'
# ]

final = ''

def calc():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    print(final)
    # закрываем окна браузера
    browser.quit()


@pytest.mark.parametrize('url_id', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_phrase(browser, url_id):
    global final
    link = f"https://stepik.org/lesson/{url_id}/step/1"
    # открываем страницу по URL
    browser.get(link)
    # вычисляем значение
    answer = calc()
    browser.implicitly_wait(5)
    # находим текстовое поле
    input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
    # вводим значение 'answer' в текстовое поле
    input_.send_keys(answer)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    # когда кнопка кликабельная, нажимаем на нее
    button.click()
    # дожидаемся фидбека о том, что ответ правильный
    # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    message_text = message.text
    expected_message = "Correct!"
    try:
        assert expected_message == message_text, f"expected {expected_message} but got {message_text}"
    except AssertionError:
        final += message_text
        raise AssertionError
