# Run test in Terminal using command:
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3$ python3 test_abs_project_2.py
# if ALL tests passed - message appears: "Everything passed"
# if any test failed: AssertionError appears and running is stopped
# (all other tests/commands after failed test will not be executed at all)

# В приведенном примере мы не увидим сообщение "Everything passed",
# так как падение любого теста вызывает выход из программы
# (test_abs2 падает и весь код после него уже не выполняется - вызывает выход из программы):

def test_abs1():
    assert abs(-42) == 42, "(test_abs1): Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "(test_abs2): Should be absolute value of a number"

def test_abs3():
    assert abs(-42) == 0, "(test_abs3): Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    test_abs2()
    test_abs3()
    print("Everything passed")

# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3$ pytest test_abs_project_2.py
# ============================================ test session starts ===============================================
# platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
# rootdir: /home/svitlana/PyTest/environments/selenium_course/session3
# collected 3 items
#
# test_abs_project_2.py .FF                                                                                [100%]
#
# ============================================== FAILURES ========================================================
# ______________________________________________ test_abs2 _______________________________________________________
#
#     def test_abs2():
# >       assert abs(-42) == -42, "(test_abs2): Should be absolute value of a number"
# E       AssertionError: (test_abs2): Should be absolute value of a number
# E       assert 42 == -42
# E        +  where 42 = abs(-42)
#
# test_abs_project_2.py:15: AssertionError
# _______________________________________________ test_abs3 _____________________________________________________
#
#     def test_abs3():
# >       assert abs(-42) == 0, "(test_abs3): Should be absolute value of a number"
# E       AssertionError: (test_abs3): Should be absolute value of a number
# E       assert 42 == 0
# E        +  where 42 = abs(-42)
#
# test_abs_project_2.py:18: AssertionError
# ================================================ short test summary info =======================================
# FAILED test_abs_project_2.py::test_abs2 - AssertionError: (test_abs2): Should be absolute value of a number
# FAILED test_abs_project_2.py::test_abs3 - AssertionError: (test_abs3): Should be absolute value of a number
# ============================================= 2 failed, 1 passed in 0.14s ======================================
