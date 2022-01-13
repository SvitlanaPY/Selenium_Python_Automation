"""
Установка Firefox и Selenium-драйвера geckodriver

До этого момента мы запускали наши тесты только в браузере Chrome, но что делать,
если нужно тестировать наше веб-приложение и в других браузерах?
При этом мы будем запускать те же тесты, но при запуске тестов указывать, на каком браузере нужно запускать тесты.

Возьмем в качестве второго браузера Firefox, так как он является вторым по популярности браузером,
и его можно запустить на любой платформе.

Запускать тесты мы хотим, указывая при запуске параметр browser_name, такой командой:
pytest -s -v --browser_name=firefox test_cmd.py

Сейчас нам придется вспомнить муки установки chromedriver из урока https://stepik.org/lesson/25969/
и повторить похожий сценарий установки браузера Firefox и Selenium-драйвера для него.

Для установки Firefox скачайте его с официального сайта и установите в вашей ОС:
https://www.mozilla.org/firefox/new/.

Selenium-драйвер для Firefox носит название geckodriver.

Скачайте последнюю версию geckodriver с сайта https://github.com/mozilla/geckodriver/releases и
распакуйте его в папку C:\geckodriver на Windows, /usr/local/bin на Ubuntu и macOS.

Для более подробной инструкции по установке geckodriver смотрите https://selenium-python.com/install-geckodriver.

Для Windows не забудьте добавить в системную переменную PATH папку
C:\geckodriver и перезапустить командную строку, чтобы путь стал доступен.

Чтобы проверить правильность установки geckodriver, выполните в интерпретаторе Python команды:
from selenium import webdriver
# инициализируем драйвер браузера.
После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()
driver.get("https://stepik.org/lesson/25969/step/8")

Если вы увидели, как запустилось новое окно браузера Firefox и открылась указанная ссылка,
то можете переходить к следующему шагу.

Если при попытке выполнения кода вы увидели подобное сообщение:
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
значит, geckodriver не установлен или к нему не прописан путь в системе.
Повторите заново действия по установке.
Если Firefox всё равно не запускается, то напишите в комментариях последовательность ваших действий и
подробный лог ошибки, чтобы мы могли вам помочь.
"""


"""
Установка geckodriver в Ubuntu: https://selenium-python.com/install-geckodriver
Скачиваем последнюю версию geckodriver с сайта https://github.com/mozilla/geckodriver/releases
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
Вытаскиваем файл из архива:
tar -xvzf geckodriver*
Даем нужные права драйверу:
sudo chmod +x geckodriver
Отправляем драйвер в папку где его будет искать Selenium:
sudo mv geckodriver /usr/local/bin/
"""

from selenium import webdriver
# инициализируем драйвер браузера.
# После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()    # для Firefox
# driver = webdriver.Chrome()   # для Chrome
driver.get("https://stepik.org/lesson/25969/step/8")
