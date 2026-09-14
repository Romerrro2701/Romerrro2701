"""Locale-aware smoke test for the Stepik Selenium course."""

from time import sleep

from selenium.webdriver.common.by import By


CATALOGUE_URL = (
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
)


def test_guest_can_see_add_to_basket_button(browser):
    browser.get(CATALOGUE_URL)
    sleep(30)

    add_to_basket_buttons = browser.find_elements(
        By.CSS_SELECTOR, ".btn-add-to-basket"
    )

    assert len(add_to_basket_buttons) == 1, (
        "The page must contain exactly one Add to basket button"
    )
