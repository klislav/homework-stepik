from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    dol = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id("book").click()
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()
finally:
    time.sleep(30)
    browser.quit()




