# main.py

import configparser

# Значение epsilon по умолчанию для всей системы
DEFAULT_EPSILON = 0.0001

def calculate(operand1, operand2, *, epsilon=DEFAULT_EPSILON):
    """
    Выполняет деление operand1 на operand2.

    Args:
        operand1 (int | float): Делимое.
        operand2 (int | float): Делитель.
        epsilon (float, optional): Точность. Должна быть в диапазоне
                                   (1e-9, 1e-1). По умолчанию 0.0001.

    Returns:
        float | None: Результат деления или None в случае деления на ноль.

    Raises:
        ValueError: Если epsilon выходит за пределы допустимого диапазона.
    """
    # 1. Проверка диапазона для epsilon
    if not (1e-9 < epsilon < 1e-1):
        raise ValueError("Epsilon должен быть в диапазоне от 1e-9 до 1e-1")

    # 2. Обработка деления на ноль
    if operand2 == 0:
        print("Ошибка: Деление на ноль!")
        return None

    # 3. Выполнение операции
    result = operand1 / operand2
    return result

def load_params(config_file='settings.ini'):
    """
    Считывает значение точности (epsilon) из конфигурационного файла.

    Args:
        config_file (str, optional): Имя файла конфигурации.
                                     По умолчанию 'settings.ini'.

    Returns:
        float: Значение epsilon из файла или значение по умолчанию,
               если файл/секция/ключ не найдены или значение некорректно.
    """
    config = configparser.ConfigParser()
    default_epsilon = DEFAULT_EPSILON

    try:
        # Пытаемся прочитать файл
        if not config.read(config_file):
            print(f"Предупреждение: Файл '{config_file}' не найден. Используется epsilon по умолчанию.")
            return default_epsilon
        
        # Пытаемся получить значение и преобразовать его в float
        epsilon_from_file = config.getfloat('settings', 'epsilon')
        return epsilon_from_file

    except configparser.NoSectionError:
        print("Предупреждение: Секция [settings] не найдена в файле. Используется epsilon по умолчанию.")
        return default_epsilon
    except configparser.NoOptionError:
        print("Предупреждение: Ключ 'epsilon' не найден в секции [settings]. Используется epsilon по умолчанию.")
        return default_epsilon
    except ValueError:
        print("Предупреждение: Значение epsilon в файле имеет неверный формат. Используется epsilon по умолчанию.")
        return default_epsilon
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при чтении файла: {e}. Используется epsilon по умолчанию.")
        return default_epsilon

# --- Пример использования ---
if __name__ == "__main__":
    print("--- Демонстрация работы ---")

    # 1. Простое деление с epsilon по умолчанию
    print(f"10 / 4 = {calculate(10, 4)}")

    # 2. Деление на ноль
    print(f"5 / 0 = {calculate(5, 0)}")
    
    # 3. Загрузка epsilon из файла и использование его в вычислениях
    # (Для этого примера сначала создайте файл settings.ini)
    print("\n--- Загрузка параметров из файла ---")
    
    # Создадим временный файл для демонстрации
    with open('settings.ini', 'w') as f:
        f.write('[settings]\n')
        f.write('epsilon = 0.005\n')

    loaded_epsilon = load_params()
    print(f"Загруженная точность (epsilon): {loaded_epsilon}")

    # Использование загруженной точности
    result = calculate(1, 3, epsilon=loaded_epsilon)
    print(f"1 / 3 с загруженным epsilon = {result}")

    # 4. Пример с некорректным epsilon
    try:
        calculate(1, 2, epsilon=0.5)
    except ValueError as e:
        print(f"\nОшибка при вызове с некорректным epsilon: {e}")
