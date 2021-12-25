"""
Задание: запуск тестов

В этом задании нам нужно разобраться в хитросплетениях маркировок.
Мы имеем файл с тестами, которые уже размечены маркерами для разных ситуаций запуска.

test_task_run_1.py:

import pytest

class TestMainPage:
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True

class TestBasket:
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True

@pytest.mark.skip
class TestBookPage:
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True

# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True


Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды:

pytest -v -m "smoke and not beta_users" lesson5_step7.py
"""

import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")

class TestMainPage:
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True

class TestBasket:
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True

@pytest.mark.skip
class TestBookPage:
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True

# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True


# (venv) svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson5$
# $ pytest -v -m "smoke and not beta_users" lesson5_step7.py
# ================= test session starts ===================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course, configfile: pytest.ini
# collected 7 items / 3 deselected / 4 selected
#
# lesson5_step7.py::TestMainPage::test_guest_can_login XPASS                                                                                                     [ 25%]
# lesson5_step7.py::TestBasket::test_guest_can_go_to_payment_page SKIPPED (not implemented yet)                                                                  [ 50%]
# lesson5_step7.py::TestBasket::test_guest_can_see_total_price PASSED                                                                                            [ 75%]
# lesson5_step7.py::TestBookPage::test_guest_can_add_book_to_basket SKIPPED (unconditional skip)                                                                 [100%]
#
# ================= 1 passed, 2 skipped, 3 deselected, 1 xpassed in 0.04s ===================
