# $ pytest -s -v lesson6_step3\!_parametrize_3.py

import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

test_links = []
with open("links_for_test") as f_:
    test_links = f_.readlines()
print("test_links: ", test_links)
#  test_links:  ['https://stepik.org/lesson/236895/step/1\n', 'https://stepik.org/lesson/236896/step/1\n', 'https://stepik.org/lesson/236897/step/1\n', 'https://stepik.org/lesson/236898/step/1\n', 'https://stepik.org/lesson/236899/step/1\n', 'https://stepik.org/lesson/236903/step/1\n', 'https://stepik.org/lesson/236904/step/1\n', 'https://stepik.org/lesson/236905/step/1']
test_links = [line.rstrip() for line in test_links]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', test_links)
def test_selenium_3_6_3(browser, url):
    link = "{}".format(url)
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    ans = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    try:
        assert "Correct!" in ans
    except:
        with open("3_6_3_test_Errors.log", "a") as f:
            f.write(ans)
        raise AssertionError('Error! See "3_6_3_test_Errors.log"')
