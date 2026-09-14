"""
2.4 Настройка ожиданий

Почему это нужно
---------------
Современные страницы подгружают элементы асинхронно. browser.get() и
find_element() не гарантируют, что конкретная кнопка уже кликабельна или нужный
текст появился. Из-за этого тесты без ожиданий становятся нестабильными.

time.sleep()
------------
time.sleep(3) ждёт ровно три секунды: это медленно, когда страница готова
раньше, и ненадёжно, когда ей нужно больше времени. В тестах используем только
для краткого ручного наблюдения, не как синхронизацию.

Implicit wait
-------------
browser.implicitly_wait(5)

Неявное ожидание влияет на каждый поиск элемента: Selenium будет повторять
поиск до пяти секунд. Оно удобно для простых учебных примеров, но скрывает
время ожидания и усложняет диагностику. Не смешиваем его с явными ожиданиями.

Explicit wait — предпочтительный вариант
-----------------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(browser, 10)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit")))
button.click()

Явное ожидание описывает конкретное условие: presence_of_element_located,
visibility_of_element_located, element_to_be_clickable, text_to_be_present_in_element
или alert_is_present. Тест продолжится сразу после выполнения условия или упадёт
с понятным TimeoutException по истечении заданного времени.
"""
