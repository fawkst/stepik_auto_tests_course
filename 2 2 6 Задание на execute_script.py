from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


LINK = 'https://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x)))
    browser.find_element(By.ID, 'robotCheckbox').click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    sleep(5)
finally:
    browser.quit()