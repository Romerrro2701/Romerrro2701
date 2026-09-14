"""
3.6 PyTest — параметризация, конфигурирование, плагины

Параметризация запускает один сценарий на нескольких наборах данных:

import pytest

@pytest.mark.parametrize("language", ["en", "ru", "es"])
def test_add_to_cart(browser, language):
    browser.get(f"https://example.com/?lang={language}")
    ...

Параметры командной строки и conftest.py
----------------------------------------
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")

@pytest.fixture
def language(request):
    return request.config.getoption("--language")

Запуск: pytest --language=ru

Так тест не хранит переменные окружения и варианты запуска в коде. Для
перезапуска нестабильных тестов используют плагины осознанно: сначала ищем
причину нестабильности, а не прячем её retries.

Конфигурация pytest.ini
-----------------------
[pytest]
addopts = -ra -q
testpaths = tests
python_files = test_*.py
"""
