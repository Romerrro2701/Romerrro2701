"""
3.4 Использование фикстур в PyTest

Фикстура — подготовка окружения, которую pytest передаёт в тест по имени.
Она уменьшает повторение и гарантирует корректный teardown.

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_title(browser):
    browser.get("https://example.com")
    assert browser.title == "Example Domain"

yield разделяет setup и teardown: всё после yield выполнится даже при падении
теста. У фикстуры может быть scope="function" (значение по умолчанию),
"class", "module", "package" или "session". Для браузера обычно безопаснее
scope="function", чтобы тесты не влияли друг на друга.

Фикстуры общего назначения принято хранить в conftest.py. Pytest находит их
автоматически, импортировать conftest.py в тесты не нужно.
"""
