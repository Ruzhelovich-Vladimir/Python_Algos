"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""


def input_n_digit_figure(n_fugere, msg=''):
    """
    'Получить n-значное число'
    :param n: - кол-во знаков в числе
    :param msg: сообщение пользователю
    :return:
    число
    None если пользователю ввел н n-значное целое число
    """
    usr_str = input(msg)

    try:  # Попытка преобраовать в вещественное число
        usr_float = float(usr_str)
    except ValueError:
        return None

    usr_int = int(usr_float)
    # Проверяем целое число, N -значное число
    if usr_float == usr_int and len(str(usr_int)) == n_fugere:
        return usr_int

    return None


if __name__ == "__main__":

    USR_DIGITAL = input_n_digit_figure(3, "Введите 3-х значное число:")

    if USR_DIGITAL is not None:
        DIGITAL_1 = USR_DIGITAL // 100
        DIGITAL_2 = (USR_DIGITAL // 10) % 10
        DIGITAL_3 = USR_DIGITAL % 10

        print(f'Сумма чисел: { DIGITAL_1 + DIGITAL_2 + DIGITAL_3 }')
        print(f'Произведение чисел: {DIGITAL_1 * DIGITAL_2 * DIGITAL_3}')
    else:
        print('Вы ввели не 3-х значное число')
