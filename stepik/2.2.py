"""
2.2 Работа с файлами, списками и js-скриптами

Выпадающие списки
------------------
Для HTML-тега <select> Selenium даёт обёртку Select:

from selenium.webdriver.support.ui import Select

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text("Python")
select.select_by_value("1")
select.select_by_index(0)

select_by_visible_text читается лучше всего, если текст — стабильная часть
интерфейса. select_by_value полезен, когда value — технический идентификатор.

JavaScript
----------
browser.execute_script("return arguments[0].scrollIntoView(true);", element)

execute_script выполняет JavaScript в контексте страницы. Это запасной
инструмент: сначала следует использовать обычные методы Selenium (click,
send_keys, WebDriverWait). JS оправдан, например, для прокрутки к элементу
или чтения значения, которое браузер не отображает обычным способом.

Загрузка файлов
---------------
Нативный диалог выбора файла не автоматизируем. Selenium передаёт абсолютный
путь прямо в элемент <input type="file">:

from pathlib import Path

file_path = Path("example.txt").resolve()
browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(str(file_path))

Такой подход работает одинаково локально и в CI, если файл заранее существует.
"""
