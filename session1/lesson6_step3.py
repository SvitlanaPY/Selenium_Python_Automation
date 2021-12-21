"""
Работа с браузером в Selenium
Если вы уже пробовали запускать примеры скриптов, то могли заметить, что браузер не всегда закрывается после
выполнения кода.
Поэтому обратите внимание на то, что необходимо явно закрывать окно браузера в нашем коде при помощи команды
browser.quit().
Каждый раз при открытии браузера browser = webdriver.Chrome() в системе создается процесс,
который останется висеть, если вы вручную закроете окно браузера.
Чтобы не остаться без оперативной памяти после запуска нескольких скриптов, всегда добавляйте к своим скриптам
команду закрытия:

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()

Важно еще пояснить разницу между двумя командами: browser.close() и browser.quit().
Какая между ними разница, ведь на первый взгляд обе они осуществляют одно и то же?

На самом деле, browser.close() закрывает текущее окно браузера.
Это значит, что если ваш скрипт вызвал всплывающее окно, или открыл что-то в новом окне или вкладке браузера,
то закроется только текущее окно, а все остальные останутся висеть.

В свою очередь browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера,
запущенные во время тестовой сессии.
Подробнее можно посмотреть здесь: Difference between webdriver.Dispose(), .Close() and .Quit():
https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit
Будьте внимательны с этими методами и, в общем случае, всегда используйте browser.quit().

Но что будет, если скрипт не дойдет до выполнения этого финального шага, а упадет с ошибкой где-то раньше?

Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,
проще всего использовать конструкцию try/finally:

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

Можете попробовать запустить оба примера и обратить внимание на разницу.

Подробно говорить об обработке исключений мы сейчас не будем, здесь важно понимать только то,
что даже если в коде внутри блока try произойдет какая-то ошибка,
то код внутри блока finally выполнится в любом случае.
Советуем добавлять такую обработку ко всем своим скриптам при выполнении задач этого и следующего модулей,
а в третьем модуле мы обсудим более лаконичные конструкции.

Если хотите узнать больше про исключения, как их кидать, ловить и как с ними жить,
то советуем к прохождению вот этот урок:  https://stepik.org/lesson/24463/step/1?unit=6771s.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
