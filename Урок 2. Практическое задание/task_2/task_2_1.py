"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def main():
    """Основная часть скрипта"""
    while True:
        try:
            usr_number = int(input('Введите натуральное число: '))
        except ValueError:
            print("Ошибка. Вы ввели не натуральное число")
            continue
        if usr_number<0:
            print("Ошибка. Вы ввели не натуральное число")
            continue
        break

    odd_count = 0
    even_count = 0
    value = usr_number
    while value > 0:
        flag = (value % 10) % 2 == 0  # Флаг чётности
        even_count += (1 if flag else 0)
        odd_count += (1 if not flag else 0)
        value = value // 10

    print(f"В числе {usr_number} всего {even_count+odd_count} цифр, из \
    которых {even_count} чётных и {odd_count} нечётных")


if __name__ == "__main__":

    main()
