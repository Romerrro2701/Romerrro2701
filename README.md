# Selenium и Python — Stepik

Учебные материалы и выполненные задания курса «Автоматизация тестирования с помощью Selenium и Python».

## Содержание

- [`stepik/`](stepik/) — конспекты, учебные примеры и песочница `test.py`;
- `conftest.py` и `test_items.py` — задание 3.6, шаг 10: тест каталога в разных языках интерфейса.

## Запуск задания 3.6

```bash
pip install pytest selenium
pytest --language=es test_items.py
```

Для проверки французского интерфейса: `pytest --language=fr test_items.py`.
