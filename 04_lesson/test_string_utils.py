import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# Тесты для метода capitalize()
def test_capitalize(utils):
    assert utils.capitalize("skypro") == "Skypro"  # Позитивный тест
    assert utils.capitalize("") == ""              # Пустая строка
    assert utils.capitalize("123abc") == "123abc"  # Цифры и буквы
    assert utils.capitalize(" hello") == " hello"  # Пробел в начале


# Тесты для метода trim()
def test_trim(utils):
    assert utils.trim("   skypro") == "skypro"     # Пробелы в начале
    assert utils.trim("skypro   ") == "skypro   "  # Пробелы в конце
    assert utils.trim("") == ""                    # Пустая строка
    assert utils.trim("    ") == ""                # Только пробелы
    assert utils.trim("\t\ttext") == "\t\ttext"    # Табы (не обрабатываются)


# Тесты для метода contains()
def test_contains(utils):
    assert utils.contains("SkyPro", "S") is True   # Символ есть
    assert utils.contains("SkyPro", "U") is False  # Символ отсутствует
    assert utils.contains("", "a") is False        # Пустая строка
    assert utils.contains("hello", "HELLO") is False  # Регистрозависимость


# Тесты для метода delete_symbol()
def test_delete_symbol(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"   # Удаление символа
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"   # Удаление подстроки
    assert utils.delete_symbol("Hello", "l") == "Heo"      # Все вхождения
    assert utils.delete_symbol("Test", "X") == "Test"      # Символ отсутствует
    assert utils.delete_symbol("", "a") == ""              # Пустая строка
