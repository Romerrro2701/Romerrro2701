"""
1.2 Запускаем браузер с помощью Selenium WebDriver

Минимальный современный шаблон
------------------------------
from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("https://example.com")
    print(driver.title)
finally:
    driver.quit()

webdriver.Chrome() создаёт сессию Chrome и возвращает объект WebDriver.
Через него выполняются команды браузеру. Метод get(url) переходит на страницу,
а quit() закрывает всё окно браузера и останавливает сессию драйвера.

Важно
------
quit() нужно вызывать в finally: блок выполнится и после успешно завершённого
сценария, и при ошибке. Иначе процессы браузера могут остаться запущенными.

В этой папке test.py использует webdriver-manager. Он скачивает или ищет
ChromeDriver сам. В актуальном Selenium 4 чаще достаточно webdriver.Chrome(),
так как Selenium Manager подбирает совместимый драйвер автоматически.
"""
