"""
Поиск элементов с помощью Selenium

find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
find_element(By.NAME, value) — поиск по атрибуту name элемента;
find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.




"""

# Практика из шага 1.6.11: тест заполняет обязательные поля формы регистрации.
# На registration1.html все поля есть, а на registration2.html отсутствует поле
# фамилии, поэтому Selenium выбросит NoSuchElementException — это и есть
# обнаруженный тестом баг.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


REGISTRATION_URL = "https://suninjuly.github.io/registration1.html"
SUCCESS_MESSAGE = "Congratulations! You have successfully registered!"


def test_required_registration_fields() -> None:
    driver = webdriver.Chrome()
    try:
        driver.get(REGISTRATION_URL)

        # Селекторы привязаны к обязательному блоку формы, поэтому не выбирают
        # одноимённые необязательные поля phone и address.
        driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys(
            "ivan@example.com"
        )
        driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        result = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        assert result.text == SUCCESS_MESSAGE
    finally:
        driver.quit()


if __name__ == "__main__":
    test_required_registration_fields()
