# $ pytest -s -v lesson6_step3\!_parametrize_my.py

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
url_id_list = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
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


@pytest.mark.parametrize('url_id', url_id_list)
def test_phrase(browser, url_id):
    global final
    link = f"https://stepik.org/lesson/{url_id}/step/1"
    # открываем страницу по URL
    browser.get(link)
    # вычисляем значение
    answer = calc()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
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
    # message_text = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    message = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    message_text = message.text
    expected_message = "Correct!"
    try:
        assert expected_message == message_text, f"expected {expected_message} but got {message_text}"
    except AssertionError:
        final += message_text
        raise AssertionError


# svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson6$
# $ pytest -s -v lesson6_step3\!_parametrize_my.py
# ================== test session starts =======================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course, configfile: pytest.ini
# collected 8 items
#
# lesson6_step3!_parametrize_my.py::test_phrase[236895]
# start browser for test..
# PASSED
# quit browser..
#
#
# lesson6_step3!_parametrize_my.py::test_phrase[236896]
# start browser for test..
# PASSED
# quit browser..
#
#
# lesson6_step3!_parametrize_my.py::test_phrase[236897]
# start browser for test..
# PASSED
# quit browser..
#
#
# lesson6_step3!_parametrize_my.py::test_phrase[236898]
# start browser for test..
# FAILED
# quit browser..
# The owls
#
# lesson6_step3!_parametrize_my.py::test_phrase[236899]
# start browser for test..
# FAILED
# quit browser..
# The owls are not
#
# lesson6_step3!_parametrize_my.py::test_phrase[236903]
# start browser for test..
# PASSED
# quit browser..
# The owls are not
#
# lesson6_step3!_parametrize_my.py::test_phrase[236904]
# start browser for test..
# PASSED
# quit browser..
# The owls are not
#
# lesson6_step3!_parametrize_my.py::test_phrase[236905]
# start browser for test..
# FAILED
# quit browser..
# The owls are not what they seem! OvO
#
#
# =============================== FAILURES ==============================
# _______________________ test_phrase[236898] ___________________________
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="dd23248747d95af9d3673898b64f47a5")>, url_id = 236898
#
#
#
#     @pytest.mark.parametrize('url_id', url_id_list)
#     def test_phrase(browser, url_id):
#         global final
#         link = f"https://stepik.org/lesson/{url_id}/step/1"
#         # открываем страницу по URL
#         browser.get(link)
#         # вычисляем значение
#         answer = calc()
#         browser.implicitly_wait(5)
#         # находим текстовое поле
#         input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
#         # вводим значение 'answer' в текстовое поле
#         input_.send_keys(answer)
#         # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
#         # когда кнопка кликабельная, нажимаем на нее
#         button.click()
#         # дожидаемся фидбека о том, что ответ правильный
#         # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
#         message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
#         message_text = message.text
# >       expected_message = "Correct!"
# E       AssertionError: expected Correct! but got The owls
# E       assert 'Correct!' == 'The owls '
# E         - The owls
# E         + Correct!
#
# lesson6_step3!_parametrize_my.py:64: AssertionError
#
# During handling of the above exception, another exception occurred:
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="dd23248747d95af9d3673898b64f47a5")>, url_id = 236898
#
#
#
#     @pytest.mark.parametrize('url_id', url_id_list)
#     def test_phrase(browser, url_id):
#         global final
#         link = f"https://stepik.org/lesson/{url_id}/step/1"
#         # открываем страницу по URL
#         browser.get(link)
#         # вычисляем значение
#         answer = calc()
#         browser.implicitly_wait(5)
#         # находим текстовое поле
#         input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
#         # вводим значение 'answer' в текстовое поле
#         input_.send_keys(answer)
#         # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
#         # когда кнопка кликабельная, нажимаем на нее
#         button.click()
#         # дожидаемся фидбека о том, что ответ правильный
#         # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
#         message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
#         message_text = message.text
#         expected_message = "Correct!"
#         try:
#             assert expected_message == message_text, f"expected {expected_message} but got {message_text}"
# >       except AssertionError:
# E       AssertionError
#
# lesson6_step3!_parametrize_my.py:67: AssertionError
# ___________________________ test_phrase[236899] _______________________________
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="401ccf7019e1a88d61af164b7920fa1f")>, url_id = 236899
#
#
#
#     @pytest.mark.parametrize('url_id', url_id_list)
#     def test_phrase(browser, url_id):
#         global final
#         link = f"https://stepik.org/lesson/{url_id}/step/1"
#         # открываем страницу по URL
#         browser.get(link)
#         # вычисляем значение
#         answer = calc()
#         browser.implicitly_wait(5)
#         # находим текстовое поле
#         input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
#         # вводим значение 'answer' в текстовое поле
#         input_.send_keys(answer)
#         # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
#         # когда кнопка кликабельная, нажимаем на нее
#         button.click()
#         # дожидаемся фидбека о том, что ответ правильный
#         # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
#         message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
#         message_text = message.text
# >       expected_message = "Correct!"
# E       AssertionError: expected Correct! but got are not
# E       assert 'Correct!' == 'are not '
# E         - are not
# E         + Correct!
#
# lesson6_step3!_parametrize_my.py:64: AssertionError
#
# During handling of the above exception, another exception occurred:
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="401ccf7019e1a88d61af164b7920fa1f")>, url_id = 236899
#
#
#
#     @pytest.mark.parametrize('url_id', url_id_list)
#     def test_phrase(browser, url_id):
#         global final
#         link = f"https://stepik.org/lesson/{url_id}/step/1"
#         # открываем страницу по URL
#         browser.get(link)
#         # вычисляем значение
#         answer = calc()
#         browser.implicitly_wait(5)
#         # находим текстовое поле
#         input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
#         # вводим значение 'answer' в текстовое поле
#         input_.send_keys(answer)
#         # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
#         # когда кнопка кликабельная, нажимаем на нее
#         button.click()
#         # дожидаемся фидбека о том, что ответ правильный
#         # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
#         message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
#         message_text = message.text
#         expected_message = "Correct!"
#         try:
#             assert expected_message == message_text, f"expected {expected_message} but got {message_text}"
# >       except AssertionError:
# E       AssertionError
#
# lesson6_step3!_parametrize_my.py:67: AssertionError
# ________________ test_phrase[236905] _______________________
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="762c9c5eb40fbbcd8a835eb159b51fe0")>, url_id = 236905
#
#
#
#     @pytest.mark.parametrize('url_id', url_id_list)
#     def test_phrase(browser, url_id):
#         global final
#         link = f"https://stepik.org/lesson/{url_id}/step/1"
#         # открываем страницу по URL
#         browser.get(link)
#         # вычисляем значение
#         answer = calc()
#         browser.implicitly_wait(5)
#         # находим текстовое поле
#         input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
#         # вводим значение 'answer' в текстовое поле
#         input_.send_keys(answer)
#         # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
#         # когда кнопка кликабельная, нажимаем на нее
#         button.click()
#         # дожидаемся фидбека о том, что ответ правильный
#         # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
#         message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
#         message_text = message.text
# >       expected_message = "Correct!"
# E       AssertionError: expected Correct! but got what they seem! OvO
# E       assert 'Correct!' == 'what they seem! OvO'
# E         - what they seem! OvO
# E         + Correct!
#
# lesson6_step3!_parametrize_my.py:64: AssertionError
#
# During handling of the above exception, another exception occurred:
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="762c9c5eb40fbbcd8a835eb159b51fe0")>, url_id = 236905
#
#
#
#     @pytest.mark.parametrize('url_id', url_id_list)
#     def test_phrase(browser, url_id):
#         global final
#         link = f"https://stepik.org/lesson/{url_id}/step/1"
#         # открываем страницу по URL
#         browser.get(link)
#         # вычисляем значение
#         answer = calc()
#         browser.implicitly_wait(5)
#         # находим текстовое поле
#         input_ = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea")
#         # вводим значение 'answer' в текстовое поле
#         input_.send_keys(answer)
#         # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#         button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
#         # когда кнопка кликабельная, нажимаем на нее
#         button.click()
#         # дожидаемся фидбека о том, что ответ правильный
#         # message_text = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
#         message = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
#         message_text = message.text
#         expected_message = "Correct!"
#         try:
#             assert expected_message == message_text, f"expected {expected_message} but got {message_text}"
# >       except AssertionError:
# E       AssertionError
#
# lesson6_step3!_parametrize_my.py:67: AssertionError
# ================ short test summary info ========================
# FAILED lesson6_step3!_parametrize_my.py::test_phrase[236898] - AssertionError
# FAILED lesson6_step3!_parametrize_my.py::test_phrase[236899] - AssertionError
# FAILED lesson6_step3!_parametrize_my.py::test_phrase[236905] - AssertionError
# ============= 3 failed, 5 passed in 101.36s (0:01:41) =============
