# Run test in Terminal using command:
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3$ python3 test_abs_project_1.py
# if test passed - message appears: "All tests passed!"
# if test failed: AssertionError: Should be absolute value of a number

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")
