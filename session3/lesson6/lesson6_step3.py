"""
Задание: параметризация тестов

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
Ваша задача — реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте:
lesson6_step3.jpg

Правильным ответом на задачу в заданных шагах является число:
import time
import math
answer = math.log(int(time.time()))

Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания,
чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания.
Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!"
Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том,
что у вас установлено правильное локальное время (https://time.is/ru/).
Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    # закрываем окна браузера
    browser.quit()

# список всех возможных ссылок/url
urls_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

# @pytest.mark.parametrize('url', urls_list)
def test_guest_should_see_login_link(browser, url):
    # открываем страницу по URL
    # link = f"{url}"
    browser.get(url)
    # вычисляем значение
    answer = calc()
    # находим текстовое поле
    input = browser.find_element(By.XPATH, '//input[@class="form-control" and @id="answer" and @required]')
    # вводим значение 'answer' в текстовое поле
    input.send_keys(answer)
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until_not(EC.element_to_be_clickable((By.ID, "verify")))
    # когда кнопка кликабельная, нажимаем на нее
    button.click()
    # дожидаемся фидбека о том, что ответ правильный
    message = browser.find_element(By.ID, "verify_message")
    assert "Correct!" in message.text

