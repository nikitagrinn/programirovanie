# test_app.py

import pytest
from main import calculate, load_params

# ======== Тесты для функции calculate ========

def test_calculate_simple_division():
    """Тест 1: 1/2, epsilon = 0.1 => 0.5"""
    assert calculate(1, 2, epsilon=0.01) == 0.5

def test_calculate_with_default_epsilon():
    """Тест 2: 1/1000 = 0.001 (используется epsilon по умолчанию)"""
    assert calculate(1, 1000) == 0.001

def test_calculate_division_by_zero():
    """Тест 3: Деление на ноль"""
    assert calculate(10, 0) is None

def test_calculate_epsilon_in_range():
    """Проверяем, что epsilon в допустимом диапазоне работает"""
    assert calculate(5, 2, epsilon=1e-5) == 2.5

def test_calculate_epsilon_out_of_range_too_high():
    """Проверяем, что epsilon > 0.1 вызывает ошибку"""
    with pytest.raises(ValueError, match="Epsilon должен быть в диапазоне"):
        calculate(1, 2, epsilon=0.5)

def test_calculate_epsilon_out_of_range_too_low():
    """Проверяем, что epsilon < 1e-9 вызывает ошибку"""
    with pytest.raises(ValueError, match="Epsilon должен быть в диапазоне"):
        calculate(1, 2, epsilon=1e-10)

# ======== Тесты для функции load_params ========

def test_load_params_file_not_found(monkeypatch, tmp_path):
    """Тест 1: Проверить ситуацию, когда файл не найден"""
    # Переходим во временную пустую директорию, где нет settings.ini
    monkeypatch.chdir(tmp_path)
    # Ожидаем, что функция вернет значение по умолчанию
    from main import DEFAULT_EPSILON
    assert load_params() == DEFAULT_EPSILON

def test_load_params_success(tmp_path):
    """Тест 2: Epsilon успешно считывается и входит в диапазон"""
    # Создаем временный config-файл
    config_file = tmp_path / "settings.ini"
    config_file.write_text("[settings]\nepsilon = 0.00123\n")
    
    # Проверяем, что функция считывает правильное значение
    assert load_params(config_file) == 0.00123

def test_load_params_bad_format(tmp_path):
    """Тест 3: Формат числа в конф. файле некорректный"""
    # Создаем файл с некорректным значением epsilon
    config_file = tmp_path / "settings.ini"
    config_file.write_text("[settings]\nepsilon = not_a_number\n")
    
    # Ожидаем, что функция вернет значение по умолчанию
    from main import DEFAULT_EPSILON
    assert load_params(config_file) == DEFAULT_EPSILON

def test_load_params_missing_section(tmp_path):
    """Тест 4: В файле отсутствует нужная секция [settings]"""
    config_file = tmp_path / "settings.ini"
    config_file.write_text("[other_section]\nepsilon = 0.01\n")
    
    from main import DEFAULT_EPSILON
    assert load_params(config_file) == DEFAULT_EPSILON

def test_load_params_missing_key(tmp_path):
    """Тест 5: В секции [settings] отсутствует ключ epsilon"""
    config_file = tmp_path / "settings.ini"
    config_file.write_text("[settings]\nanother_key = 123\n")
    
    from main import DEFAULT_EPSILON
    assert load_params(config_file) == DEFAULT_EPSILON
