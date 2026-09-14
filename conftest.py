"""PyTest configuration for Stepik block 3, lesson 3.6, step 10."""

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Browser interface language, for example: es, fr, ru",
    )


@pytest.fixture(scope="function")
def browser(request):
    """Start Chrome configured with the language passed to PyTest."""
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language},
    )
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
