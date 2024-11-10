from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep


LINK = 'http://suninjuly.github.io/file_input.html'


def get_file_path(filename):
    abs_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(abs_path, filename)


try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    browser.find_element(By.NAME, 'firstname').send_keys('Alex')
    browser.find_element(By.NAME, 'lastname').send_keys('Balck')
    browser.find_element(By.NAME, 'email').send_keys('test@test')

    browser.find_element(By.ID, 'file').send_keys(get_file_path('../file.txt'))

    browser.find_element(By.CSS_SELECTOR, '.btn').click()

    sleep(5)
finally:
    browser.quit()