"""
3.5 PyTest — маркировка

Маркеры группируют тесты и позволяют выбирать нужный набор при запуске:

import pytest

@pytest.mark.smoke
def test_login():
    ...

pytest -m smoke

Пользовательский маркер регистрируем в pytest.ini, иначе pytest выдаст
предупреждение:

[pytest]
markers =
    smoke: critical quick checks

Пропуск и ожидаемое падение
---------------------------
@pytest.mark.skip(reason="Feature is not released")
def test_future_feature():
    ...

@pytest.mark.xfail(reason="Known bug #123", strict=True)
def test_known_defect():
    ...

skip означает «тест сейчас не запускался». xfail означает «падение ожидаемо».
strict=True полезен: неожиданно успешный xfail (XPASS) станет ошибкой и
подсветит, что известный дефект мог быть исправлен.
"""
