from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


LINK = 'https://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x)))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    sleep(5)
finally:
    browser.quit()