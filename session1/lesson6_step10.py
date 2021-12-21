"""
Уникальность селекторов: часть 2
Попробуем реализовать один из автотестов из предыдущего шага.
Вам дана страница с формой регистрации.
Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *:
First name, last name, email.
Текст для полей может быть любым.
Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
с текстом на странице, которая открывается после регистрации.
Для сравнения воспользуемся стандартной конструкцией assert из языка Python.

Ниже дан шаблон кода, который вам нужно использовать для своего теста.
Не забывайте, что селекторы должны быть уникальными.

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

Углубимся немного в использовании конструкции assert из данного примера,
Если результат проверки "Поздравляем! Вы успешно зарегистрировались!" == welcome_text вернет значение False,
то далее выполнится код assert False.
Он бросит исключение AssertionError и номер строки, в которой произошла ошибка.
Если код написан правильно и работал ранее, то такой результат равносилен тому,
что наш автотест обнаружил баг в тестируемом веб-приложении.
Если результат проверки вернет True, то выполнится выражение assert True.
В этом случае код завершится без ошибок — тест прошел успешно.
Подробнее про использование assert в коде мы поговорим в третьем модуле этого курса.

В этом задании нет автоматических проверок вашего кода.
Просто убедитесь, что ваш тест проходит успешно, и вы не видите AssertionError в результатах работы вашего кода.

Замечание
В этом примере мы использовали метод time.sleep(1), чтобы дождаться загрузки следующей страницы, прежде чем выполнять проверки.
Если вы будете запускать код без этого метода, ваш код может внезапно упасть, хотя проходил ранее.
Без использования такой паузы WebDriver может перейти к поиску тега h1 слишком рано, когда новая страница еще не загрузилась. В таком случаем будем видеть в терминале ошибку:

NoSuchElementException... Unable to locate element: {"method":"tag name","selector":"h1"}
Метод time.sleep(1) говорит Python подождать 1 секунду, прежде чем выполнять следующую строчку кода.
Если вы всё равно видите эту ошибку, просто увеличьте количество секунд ожидания.

Проблема со своевременным поиском элемента — одна из самых больших проблем,
которую приходится решать при разработке автотестов для UI.
В условиях постоянно изменяющейся скорости сетевого соединения и
неравномерности нагрузки на серверы скорость загрузки страницы может сильно варьироваться.
Еще одним фактором, влияющим на стабильность работы тестов, является принцип асинхронности выполнения кода JavaScript.
На простых страницах вы можете этого и не заметить,
но на функционально богатых страницах время появления элементов страницы может быть непредсказуемо.
Хорошо было бы организовать тесты так, чтобы не сложилось ситуации,
когда они не проходят по причине нестабильной скорости интернета или других причин, которые от нас не зависят.

Решать эту проблему с помощью time.sleep() считается плохой практикой,
так как заранее трудно указать нужное время ожидания.
Если выставить слишком большое время ожидания, то тесты будут идти неоправданно долго.
В дальнейших уроках мы рассмотрим более красивые и эффективные способы решения этой проблемы,
а пока будем использовать time.sleep() из-за его простоты и наглядности.
"""

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_class_name("form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("form-control.second")
    input2.send_keys("Popovych")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("ivan_popovych@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
