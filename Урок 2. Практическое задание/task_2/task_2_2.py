"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def usr_number(msg):
    """
    :param msg: Сообщение пользователю
    :return: Натуральное число
    """
    try:
        number = int(input(msg))
    except ValueError:
        print("Ошибка. Вы ввели не натуральное число")
        return usr_number(msg)
    if number < 0:
        print("Ошибка. Вы ввели не натуральное число")
        return usr_number(msg)
    return number


def count_num_even_odd(number):
    """
    :param number:
    :return: Кол-во чётных и не чётных чисел в натуральном числе
    """
    even_count = 0
    odd_count = 0

    if number > 0:
        flag = (number % 10) % 2 == 0  # Флаг чётности
        even_count, odd_count = count_num_even_odd(number // 10)
        even_count += (1 if flag else 0)
        odd_count += (1 if not flag else 0)
        return even_count, odd_count
    return even_count, odd_count


def main():
    """Основная часть скрипта"""

    number = usr_number('Введите натуральное число: ')

    even_count, odd_count = count_num_even_odd(number)

    print(f"В числе {number} всего {even_count+odd_count} цифр, из \
которых {even_count} чётных и {odd_count} нечётных")


if __name__ == "__main__":

    main()
