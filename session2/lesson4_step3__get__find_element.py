"""
Как работают методы get и find_element
Разберем еще один простой тест на WebDriver, проверяющий работу кнопки.

Тестовый сценарий выглядит так:

Открыть страницу http://suninjuly.github.io/wait1.html
Нажать на кнопку "Verify"
Проверить, что появилась надпись "Verification was successful!"
Для открытия страницы мы используем метод get, затем находим нужную кнопку с помощью одного из методов
find_element_by_ и нажимаем на нее с помощью метода click.
Далее находим новый элемент с текстом и проверяем соответствие текста на странице ожидаемому тексту.

Вот как выглядит код автотеста:

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text


Попробуйте сначала выполнить тест вручную, а затем запустить автотест.
В первом случае, вы завершите тест успешно,
во втором случае автотест упадет с сообщением NoSuchElementException для элемента c id="verify".
Почему так происходит?

Команды в Python выполняются синхронно, то есть, строго последовательно.
Пока не завершится команда get, не начнется поиск кнопки.
Пока кнопка не найдена, не будет сделан клик по кнопке и так далее.

Но тест будет работать абсолютно стабильно, только если в данной веб-странице не используется JavaScript
(что маловероятно для современного веба).

Метод get дожидается информации от браузера о том, что страница загружена,
и только после этого наш тест переходит к поиску кнопки.

Если страница интерактивная, то браузер будет считать, что страница загружена,
при этом продолжат выполняться загруженные браузером скрипты.
Скрипт может управлять появлением кнопки на странице и показывать ее, например, с задержкой,
чтобы кнопка красиво и медленно возникала на странице.
В этом случае наш тест упадет с уже известной нам ошибкой NoSuchElementException, так как в момент выполнения команды
button = browser.find_element_by_id("verify") элемент с id="verify" еще не отображается на странице.
На данной странице пауза перед появлением кнопки установлена на 1 секунду,
метод find_element_by_id() сделает только одну попытку найти элемент и в случае неудачи уронит наш тест.
"""

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
