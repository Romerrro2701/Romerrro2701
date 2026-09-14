"""Stepik 3.2, step 13: запуск двух тестов через unittest.

Первый адрес содержит все обязательные поля, второй специально содержит
ошибку в разметке. Поэтому в итоговом отчёте unittest один тест успешен,
а второй завершается с NoSuchElementException.
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


EXPECTED_MESSAGE = "Congratulations! You have successfully registered!"


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def fill_required_fields(self):
        self.browser.find_element(By.CSS_SELECTOR, "input.first[required]").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, "input.second[required]").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, "input.third[required]").send_keys("ivan@example.com")

    def test_registration_page_has_all_required_fields(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.fill_required_fields()
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(EXPECTED_MESSAGE, welcome_text)

    def test_broken_registration_page(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.fill_required_fields()
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(EXPECTED_MESSAGE, welcome_text)


if __name__ == "__main__":
    unittest.main()
