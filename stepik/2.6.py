"""
2.6 Полезные ссылки к первому и второму модулям

Основные источники
------------------
* Официальная документация Selenium: https://www.selenium.dev/documentation/
* Ожидания в Selenium: https://www.selenium.dev/documentation/webdriver/waits/
* Локаторы в Selenium Python: https://www.selenium.dev/documentation/webdriver/elements/locators/
* Справочник по хорошим локаторам: http://barancev.github.io/good-locators/

Как пользоваться ресурсами
--------------------------
1. Сначала сформулировать наблюдаемое поведение и ожидаемый результат.
2. Найти нужный API в официальной документации Selenium.
3. Проверить маленькую гипотезу в test.py.
4. Перенести устойчивый пример и вывод в файл соответствующей темы.

Замечание о старых материалах
-----------------------------
Курс использует устаревшие имена вроде find_element_by_id. В установленном
Selenium 4 следует писать современный вариант:

from selenium.webdriver.common.by import By

element = browser.find_element(By.ID, "user-name")

Так конспект остаётся применимым к текущим версиям Selenium.
"""
