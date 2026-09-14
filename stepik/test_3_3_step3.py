"""Stepik 3.3, step 3: те же проверки регистрации, запущенные PyTest.

Имя файла начинается с ``test_``, чтобы PyTest обнаружил его автоматически.
Запуск из этой папки:
    ./venv/bin/python -m pytest test_3_3_step3.py
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


EXPECTED_MESSAGE = "Congratulations! You have successfully registered!"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def fill_required_fields(driver):
    driver.find_element(By.CSS_SELECTOR, "input.first[required]").send_keys("Ivan")
    driver.find_element(By.CSS_SELECTOR, "input.second[required]").send_keys("Petrov")
    driver.find_element(By.CSS_SELECTOR, "input.third[required]").send_keys("ivan@example.com")


def test_registration_page_has_all_required_fields(browser):
    browser.get("http://suninjuly.github.io/registration1.html")
    fill_required_fields(browser)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    assert browser.find_element(By.TAG_NAME, "h1").text == EXPECTED_MESSAGE


def test_broken_registration_page(browser):
    browser.get("http://suninjuly.github.io/registration2.html")
    fill_required_fields(browser)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    assert browser.find_element(By.TAG_NAME, "h1").text == EXPECTED_MESSAGE
