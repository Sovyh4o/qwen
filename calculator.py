"""
Простой консольный калькулятор
Поддерживает операции: +, -, *, /
"""

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def calculate(a, operator, b):
    """Выполняет операцию над двумя числами"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator not in operations:
        raise ValueError(f"Неподдерживаемая операция: {operator}")
    
    return operations[operator](a, b)

def main():
    """Основная функция программы"""
    print("=== Простой калькулятор ===")
    print("Поддерживаемые операции: +, -, *, /")
    print("Введите 'q' для выхода\n")
    
    while True:
        try:
            user_input = input("Введите выражение (например, 5 + 3): ")
            
            if user_input.lower() == 'q':
                print("До свидания!")
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                print("Ошибка: введите выражение в формате 'число оператор число'")
                continue
            
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
            
            result = calculate(a, operator, b)
            print(f"Результат: {result}\n")
            
        except ValueError as e:
            print(f"Ошибка: {e}\n")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}\n")

if __name__ == "__main__":
    main()
