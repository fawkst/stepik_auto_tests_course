from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


LINK = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.alert.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)

    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.TAG_NAME, 'button').click()
    sleep(5)
finally:
    browser.quit()