from selenium import webdriver
import time
import os
import math
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    window_after = browser.window_handles[1]    # записываем второе окно в переменную
    browser.switch_to.window(window_after)      # передаем управление второй вкладке
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
