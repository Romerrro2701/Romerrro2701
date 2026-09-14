"""1.6, шаг 11: уникальные CSS-селекторы и поиск регрессионного дефекта.

Запуск:
    ./venv/bin/python 1.6_step11.py

По умолчанию тест проходит на registration1.html. Чтобы увидеть ожидаемое
падение NoSuchElementException на дефектной версии, передай второй URL:
    ./venv/bin/python 1.6_step11.py http://suninjuly.github.io/registration2.html
"""

from sys import argv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


WORKING_URL = "http://suninjuly.github.io/registration1.html"
BROKEN_URL = "http://suninjuly.github.io/registration2.html"


def fill_required_fields(browser: webdriver.Chrome) -> None:
    """Заполняет три обязательных поля только в первом блоке формы."""
    browser.find_element(By.CSS_SELECTOR, "input.first[required]").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input.second[required]").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input.third[required]").send_keys("ivan@example.com")


def register(url: str) -> None:
    """Проверяет успешную регистрацию по переданному адресу."""
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        fill_required_fields(browser)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        WebDriverWait(browser, 5).until(EC.url_contains("registration_result"))
        result = browser.find_element(By.TAG_NAME, "h1").text
        assert result == "Congratulations! You have successfully registered!", result
    finally:
        browser.quit()


if __name__ == "__main__":
    # Первый URL проходит. На BROKEN_URL нет input.second[required], поэтому
    # Selenium выбрасывает NoSuchElementException — тест обнаруживает регрессию.
    register(argv[1] if len(argv) > 1 else WORKING_URL)
