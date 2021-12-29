"""
Загрузка файлов

Если нам понадобится загрузить файл на веб-странице, мы можем использовать уже знакомый нам метод send_keys.
Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.

Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — os.
В этом случае ваш код не будет зависеть от операционной системы, которую вы используете.
Добавление файла будет работать и на Windows, и на Linux, и даже на MaсOS.

Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт,
который вы запускаете:

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)
Попробуйте добавить в файл отдельно команды print(os.path.abspath(__file__))
и
print(os.path.abspath(os.path.dirname(__file__))) и посмотрите на разницу.
Подробнее о методах модуля os можете почитать самостоятельно в документации: https://docs.python.org/3/library/os.path.html. Обратите внимание, что это будет работать только при запуске кода из файла, в интерпретаторе не сработает.

Если совсем непонятно что происходит, пример:

Допустим, мы написали код скрипта и сохранили код в lesson2_step7__load_file.py в свой локальной папке
D:\stepik_homework. Активируем виртуальное окружение и запускаем его python lesson2_step7__load_file.py.
В таком случае конструкция os.path.abspath(os.path.dirname(__file__)) вернет нам путь до директории файла с кодом,
то есть D:\stepik_homework. В эту же папку кладем файл, который хотим прикрепить, то есть file.txt.
Тогда, после выполнения команды:

file_path = os.path.join(current_dir, 'file.txt')

В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'.
Фишка в том, что если мы файлы lesson2_step7__load_file.py вместе с file.txt перенесем в другую папку,
или на компьютер с другой ОС, то такой код без правок заработает и там.

Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file".
Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path).
"""
import os
from selenium import webdriver
import time

print("1: ", os.path.abspath(__file__))
print("2: ", os.path.abspath(os.path.dirname(__file__)))

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')
print("file_path: ", file_path)

try:
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    # (открытие браузера)
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    # Метод get() сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print('current_dir: ', current_dir)   # /home/svitlana/PyTest/environments/selenium_course/session2
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    print('file_path: ', file_path)   # /home/svitlana/PyTest/environments/selenium_course/session2/file.txt

    input1 = browser.find_element_by_xpath('//input[@id="answer" and @class="form-control" and @required]')
    # загружаем файл
    input1.send_keys(file_path)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
