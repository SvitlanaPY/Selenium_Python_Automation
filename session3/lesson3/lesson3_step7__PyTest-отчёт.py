"""
PyTest — отчёты
Вы могли заметить, что PyTest позволяет генерировать подробный отчёт
с поддержкой цветовых схем и форматированием прямо из коробки.

Давайте еще раз запустим наши тесты с помощью unittest и PyTest, чтобы сравнить выводимый результат.

Мы видим, что в PyTest-отчёте упавший тест выделен красным шрифтом, что делает разбор логов более приятным занятием.

unittest:
s3_lesson3_step7_1.png

PyTest:
s3_lesson3_step7_2.png

Если запустить PyTest с параметром -v (verbose, то есть подробный),
то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения:
s3_lesson3_step7_3.png

Другие полезные команды для манипуляции выводом тестов PyTest можно найти по ссылке:
https://gist.github.com/amatellanes/12136508b816469678c2

"""