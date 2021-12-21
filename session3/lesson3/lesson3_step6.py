"""
Задание: запуск тестов
Соискатель прислал тестовый проект в качестве тестового задания на вакансию в вашу компанию.

Содержимое самих файлов выглядит примерно так:
I.  tests_for_pytest/test_main_page:
    # номер 1
    def main_page_buttons(browser):

    # номер 2
    def test_main_page_navbar(browser):

II. smoke_tests/login.py:

    # номер 3
    def test_guest_can_login(browser, language):

    # номер 4
    class TestLogin(object):
        def test_guest_should_see_login_link(self, browser, language):

III. (корневая директория проекта) test_regression.py:

    class TestLessonCreate():
        # номер 5
        def test_create_lesson(self, browser):

        # номер 6
        def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):


    class CourseCreate():
        # номер 7
        def test_create_course(self, browser):

    # номер 8
    def test_guest_can_open_new_course(browser):


Вы пытаетесь запустить тесты из директории, в которой содержится проект test_project, с помощью PyTest командой:
pytest test_project

Какие тестовые методы будут найдены и выполнены PyTest?
Ответ: #5, #8

"""