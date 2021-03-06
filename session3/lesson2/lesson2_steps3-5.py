"""     step3     """
"""
Юнит-тесты и интеграционные тесты
Если вы работаете в тестировании, то уже знаете разницу между юнит-тестами и интеграционными тестами.
Юнит-тесты проверяют очень маленький кусок кода, обычно конкретную функцию, и чаще всего их пишут разработчики,
которые хорошо понимают возможные крайние случаи для своего стека технологий.

Интеграционные тесты проверяют взаимодействие сразу нескольких систем.
Они могут создаваться и поддерживаться как разработчиками и тестировщиками, так и аналитиками
(если для них разработан удобный фреймворк для написания тестов).

Юнит-тесты всегда автоматизированы, так как проверяют непосредственно работу кода.
Интеграционные тесты могут быть ручными и автоматизированными.
Иногда выделяют отдельную категорию end-to-end (е2е) тестов, которые проверяют полный стек технологий приложения и
пользовательский сценарий взаимодействия с приложением как с черным ящиком.
Если говорить про UI-тесты, которые разрабатываются с помощью Selenium,
то их стоит отнести к разряду end-to-end тестов, так как они проверяют совместную работу всех систем web-продукта:
--работу frontend и backend,
--работу базы данных,
--дополнительные сервисы, такие как аналитика, платежные системы и так далее.

Подробно про разные типы автотестов мы говорить не будем, но советуем вам изучить теорию самостоятельно.
Вот, например, отличная и подробная статья: Пирамида тестов на практике (https://habr.com/ru/post/358950/)
"""



"""    step4    """
"""
пирамида тестирования:
https://habr.com/ru/post/358950/
https://ucarecdn.com/7ac04571-58c9-4bcb-8e30-127f8b22e464/

Отсортируйте типы тестов по их рекомендованному количеству в проекте, начиная с наименьшего количества.
Низ пирамиды (наибольшее количество) — это конец списка, внизу экрана:

1. ручные исследовательские тесты
2. автоматизированные end-to-end тесты
3. интеграционные тесты
4. юнит-тесты
"""




"""    step5    """
"""
Структура теста
Для написания UI-тестов можно использовать те же возможности Python, что и для написания юнит-тестов, которые создаются разработчиками. 

Любой тест должен содержать:

Входные данные.
Тестовый сценарий, то есть набор шагов, которые надо выполнить для получения результата.
Проверка ожидаемого результата.
Давайте обсудим, как именно можно производить проверки. 
"""
