"""
Проверка ожидаемого результата
Как можно проверить ожидаемый результат?
Для этого используется встроенная в Python инструкция assert, которая проверяет истинность утверждений.
assert True не приводит к выводу дополнительных сообщений, а вот assert False вызовет исключение AssertionError.

Рассмотрим работу assert на примере встроенной функции abs(), которая возвращает абсолютное значение числа по модулю.
Для этого активируйте созданное ранее виртуальное окружение и запустите интерпретатор Python.
Например, для Linux выполните:

source selenium_env/bin/activate
python

Теперь будем вводить приведенные ниже команды и смотреть на результат их выполнения.

Если значение выражения истинно, то в консоли не должно появиться дополнительных сообщений.

Выполним:
assert abs(-42) == 42

Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки,
в которой произошла ошибка, а также тип ошибки AssertionError:
assert abs(-42) == -42

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

Простое сообщение AssertionError не очень информативно.
Когда тестов становится много, бывает сложно вспомнить, что именно мы проверяем в данном тесте.
Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение,
которое будет выведено в случае ошибки проверки результата:

assert abs(-42) == -42, "Should be absolute value of a number"
----------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be absolute value of a number

"""
assert abs(-42) == 42
# # значение выражения истинно, поетому в консоли нету дополнительных сообщений.

# assert abs(-42) == -42
# # Traceback (most recent call last):
# #   File "<stdin>", line #, in <module>
# #     assert abs(-42) == -42
# # AssertionError


# assert abs(-42) == -42, "Should be absolute value of a number"
# # Traceback (most recent call last):
# #   File "<stdin>", line #, in <module>
# #     assert abs(-42) == -42, "Should be absolute value of a number"
# # AssertionError: Should be absolute value of a number
