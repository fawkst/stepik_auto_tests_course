from selenium.webdriver.common.by import By
from time import sleep
import pytest


LINKS = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture
def auth(browser, link):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()
    browser.find_element(By.NAME, 'login').send_keys('EMAIL')
    browser.find_element(By.NAME, 'password').send_keys('PASS')
    browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
    sleep(1)


@pytest.mark.parametrize('link', LINKS)
def test_link(browser, link, answer, auth):
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    assert browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text == 'Correct!'

