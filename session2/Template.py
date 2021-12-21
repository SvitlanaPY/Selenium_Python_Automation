from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_radio_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_radio_checked)
    # value of people radio:  true
    assert people_radio_checked == "true", "People radio is not selected by default"
    # або можна записати ще іншим способом:
    # assert people_radio_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_radio_checked)
    # value of robots radio:  None
    assert robots_radio_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
