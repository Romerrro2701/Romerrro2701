"""
2.3 Работа с окнами

Alerts
------
JavaScript-диалог не является обычным HTML-элементом. С ним работаем через
switch_to.alert:

alert = browser.switch_to.alert
print(alert.text)
alert.accept()       # OK
# alert.dismiss()    # Cancel
# alert.send_keys("text")  # только для prompt

Не ищем alert через CSS/XPath. Перед switch_to.alert часто требуется явное
ожидание alert_is_present(), иначе Selenium может обратиться к нему раньше
появления диалога.

Вкладки и окна
--------------
current_window = browser.current_window_handle
old_windows = browser.window_handles

# действие, которое откроет новую вкладку
browser.find_element(By.CSS_SELECTOR, ".open-new-window").click()

new_window = next(handle for handle in browser.window_handles if handle not in old_windows)
browser.switch_to.window(new_window)

window_handles возвращает список идентификаторов открытых окон. Его порядок не
нужно считать гарантированным: надёжнее сохранить набор старых окон и найти
новый идентификатор. После работы можно вернуться так:

browser.close()
browser.switch_to.window(current_window)
"""
