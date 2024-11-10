from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep


link = 'https://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    input_form = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_form.send_keys(calc(x))

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()
finally:
    sleep(5)
    browser.quit()