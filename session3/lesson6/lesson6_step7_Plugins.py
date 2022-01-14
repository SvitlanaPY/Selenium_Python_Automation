"""
Плагины и перезапуск тестов

Для PyTest написано большое количество плагинов:
https://docs.pytest.org/en/latest/explanation/flaky.html?highlight=plugins#plugins,
то есть дополнительных модулей, которые расширяют возможности этого фреймворка.

Полный список доступных плагинов доступен здесь:
https://docs.pytest.org/en/latest/reference/plugin_list.html

Рассмотрим еще одну проблему, с которой вы обязательно столкнетесь,
когда будете писать end-to-end тесты на Selenium.

Flaky-тесты или "мигающие" авто-тесты,
т.е. такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов,
могут иногда падать, хотя всё остальное время они проходят успешно.

Это может происходить в момент прохождения тестов из-за одновременного обновления сайта,
из-за сетевых проблем или странных стечений обстоятельств.

Конечно, надо стараться исключать такие проблемы и искать причины возникновения багов,
но в реальном мире бывает, что это требует слишком много усилий.

Поэтому мы будем перезапускать упавший тест, чтобы еще раз убедиться,
что он действительно нашел баг, а не упал случайно.

Это сделать очень просто. Для этого мы будем использовать плагин pytest-rerunfailures.

Сначала установим плагин в нашем виртуальном окружении.
После установки плагин будет автоматически найден PyTest,
и можно будет пользоваться его функциональностью без дополнительных изменений кода:
pip install pytest-rerunfailures

Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
"--reruns n", где n — это количество перезапусков.

Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным.

Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.

Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста.
Можете почитать подробнее про настройку вывода в документации PyTest:
https://docs.pytest.org/en/stable/usage.html#modifying-python-traceback-printing

pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

Давайте напишем два теста: один из них будет проходить, а другой — нет.
Посмотрим, как выглядит перезапуск.

test_rerun.py:
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

Мы увидим сообщение: "1 failed, 1 passed, 1 rerun in 9.20s",
то есть упавший тест был перезапущен, но при втором запуске тоже упал.
Если бы во второй раз мигающий тест все-таки прошёл успешно, то мы бы увидели сообщение:
"2 passed, 1 rerun in 9.20s", и итоговый результат запуска всех тестов считался бы успешным.

"""

"""
ModifyingPythonTracebackPrinting.txt

Modifying Python traceback printing
Examples for modifying traceback printing:

pytest --showlocals     # show local variables in tracebacks
pytest -l               # show local variables (shortcut)
pytest --tb=auto        # (default) 'long' tracebacks for the first and last entry, 
                          but 'short' style for the other entries
pytest --tb=long        # exhaustive, informative traceback formatting
pytest --tb=short       # shorter traceback format
pytest --tb=line        # only one line per failure
pytest --tb=native      # Python standard library formatting
pytest --tb=no          # no traceback at all
pytest --full-trace     # causes very long traces to be printed on error (longer than --tb=long).
                          By using this option you make sure a trace is shown. 
                          It also ensures that a stack trace is printed on KeyboardInterrupt (Ctrl+C). 
                          This is very useful if the tests are taking too long and you interrupt them with Ctrl+C 
                          to find out where the tests are hanging. 
                          By default no output will be shown (because KeyboardInterrupt is caught by pytest).
"""

"""
DetailedSummaryReport.txt

Detailed summary report
The -r flag can be used to display a “short test summary info” at the end of the test session, 
making it easy in large test suites to get a clear picture of all failures, skips, xfails, etc.

It defaults to fE to list failures and errors.

The -r options accepts a number of characters after it, with a used above meaning “all except passes”.
Here is the full list of available characters that can be used:
f - failed
E - error
s - skipped
x - xfailed
X - xpassed
p - passed
P - passed with output

Special characters for (de)selection of groups:
a - all except pP
A - all
N - none, this can be used to display nothing (since fE is the default)
More than one character can be used, so for example to only see failed and skipped tests, you can execute:
e.g. 
$ pytest -rfs
$ pytest -ra

Using p lists the passing tests, whilst P adds an extra section “PASSES” with those tests that passed 
but had captured output:
$ pytest -rpP


Example:

# content of test_example.py
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

"""