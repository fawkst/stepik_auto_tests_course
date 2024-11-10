from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


LINK = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    layouts = browser.window_handles
    browser.switch_to.window(layouts[1])

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    sleep(5)
finally:
    browser.quit()
