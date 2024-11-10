from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
from time import sleep


LINK = 'https://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element(By.ID, 'book').click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()
    sleep(5)
finally:
    browser.quit()