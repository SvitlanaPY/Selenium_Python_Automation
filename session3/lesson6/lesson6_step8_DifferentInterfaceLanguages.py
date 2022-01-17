"""
Запуск автотестов для разных языков интерфейса
Цель: научиться запускать автотесты для разных локалей, т.е. для разных языков интерфейсов.

Мы уже запускали автотесты для разных языков в одном из предыдущих шагов,
используя параметризацию с помощью разных ссылок,
но такой подход сложно масштабировать на большое количество тестов.
Давайте сделаем так, чтобы сервер сам решал, какой язык интерфейса нужно отобразить, основываясь на данных браузера.
Браузер передает данные о языке пользователя через запросы к серверу,
указывая в Headers (заголовке запроса) параметр accept-language.
Если сервер получит запрос с заголовком {accept-language: ru, en},
то он отобразит пользователю русскоязычный интерфейс сайта.
Если русский язык не поддерживается, то будет показан следующий язык из списка,
в данном случае пользователь увидит англоязычный интерфейс.
Это, кстати, примерно то же самое, что и выставить предпочтительный язык в настройках своего браузера:
s3_lesson6_InterfaceLangs.png

Чтобы указать язык браузера с помощью WebDriver,
используйте класс Options и метод add_experimental_option, как указано в примере ниже:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)


Для Firefox объявление нужного языка будет выглядеть немного иначе:

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)


В конструктор webdriver.Chrome или webdriver.Firefox вы можете добавлять разные аргументы,
расширяя возможности тестирования ваших веб-приложений:
можно указывать прокси-сервер для контроля сетевого трафика или запускать разные версии браузера,
указывая локальный путь к файлу браузера.

Предполагаем, что эти возможности вам понадобятся позже и вы сами сможете найти настройки для этих задач.
"""

# Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)


# Firefox
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
