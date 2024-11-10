from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep


LINK = 'http://suninjuly.github.io/selects1.html'


try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    answer = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)
    dropdown = Select(browser.find_element(By.TAG_NAME, 'select'))
    dropdown.select_by_value(str(answer))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(5)
    browser.quit()