import time
from selenium import webdriver

'''Проверить что в форме можно залогиниться заполнив только обязательные поля'''

# link = 'http://suninjuly.github.io/registration1.html'
link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем только обязательные поля. Необходимо проверить селекторы на уникальность
    first_name_req = browser.find_element_by_css_selector('input.form-control.first:required').send_keys('Sasha')
    second_name_req = browser.find_element_by_css_selector('input.form-control.second:required').send_keys('O')
    email_req = browser.find_element_by_css_selector('input.form-control.third:required').send_keys('test@test.ru')
    # Нажимаем кнопку
    button_submit = browser.find_element_by_css_selector('button.btn').click()
    # Ищем заголовок на новой странице и сравниваем его с требуемым
    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name('h1')
    assert welcome_text.text == 'Congratulations! You have successfully registered!'
finally:
    time.sleep(2)
    browser.quit()
