"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def main():
    """Основная часть скрипта"""
    while True:
        try:
            usr_number = int(input("Введите натуральное число: "))
        except ValueError:
            print("Ошибка. Вы ввели не натуральное число")
            continue
        if usr_number < 0:
            print("Ошибка. Вы ввели не натуральное число")
            continue
        break

    result = 0
    while usr_number > 0:
        result = result * 10 + usr_number % 10
        usr_number = usr_number // 10

    print(f"Перевернутое число: {result}")


if __name__ == "__main__":

    main()
