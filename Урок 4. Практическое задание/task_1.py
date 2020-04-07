"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

""" ЗАДАНИЕ ИЗ 2-го урока
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""

# Проверяю только часть задачи - рекурсивную функцию и цикл, правую часть
# не имеет смысла смотреть, т.к. она имеет сложность О(1), т.к.
# не зависомо от n кол-во операций будет постоянной, она равна 3

# Сложность данной функции О(n) - количество операций будет линейно расти


def get_left_sum_7_1(n_value):
    """
    Функция расчёта левой части уравления
    :param n_value:
    :return:
    """
    summa = 0
    elem = 1
    while elem <= n_value:
        summa += elem
        elem += 1

    return summa

# Сложность данной функции О(n) - количество операций бодет линейно расти


def get_left_sum_7_1_1(n_value):
    """
    Функция расчёта левой части уравления
    :param n_value:
    :return:
    """
    return sum([inx for inx in range(n_value)])


def get_left_sum_7_2(n_value, elem=1, summa=0):
    """
    Функция расчёта левой части уравления
    :param n_value:
    :return:
    """

    if elem <= n_value:
        summa += elem
        elem += 1
        return get_left_sum_7_2(n_value, elem, summa)
    return summa

def inverted_num_recurs(number):
    """
    :param number: Натуральное число
    :return: Перевернутое число
    """
    len_num = len(str(number))  # длинна числа в разрядах

    if len_num > 2:  # ПЕРЕВОРАЧИВАЕМ ЧИСЛО БОЛЬШЕ 99
        return int((number % 10) * (10 ** (len_num - 1)) +
                   inverted_num_recurs((number // 10) % (10 ** (len_num - 2))) * 10 +
                   (number // (10 ** (len_num - 1)) % 10))
    if len_num == 2:  # ПЕРЕВОРАЧИВАЕМ ЧИСЛО ОТ 10 ДО 99. КОНЕЦ РЕКУРСИИ
        return int((number % 10) * (10 ** (len_num - 1)) +
                   (number // (10 ** (len_num - 1)) % 10))
    return number  # ПЕРЕВОРАЧИВАЕМ ЧИСЛО ОТ 0 ДО БОЛЬШЕ 9. КОНЕЦ РЕКУРСИИ

def inverted_num_series(number):
    """
    Инвертирует число
    :param number:
    :return:
    """
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number = number // 10

    return result

def inverted_num_series(number):
    """
    Инвертирует число
    :param number:
    :return:
    """
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number = number // 10

    return result

def inverted_num_list(number):
    """
    Инвертирует число

    :param number:
    :return:
    """

    result = int("".join(list(reversed(list(str(number))))))

    return result

if __name__ == '__main__':

    from timeit import Timer
    import sys

    RECURSION_LIMIT = sys.getrecursionlimit()
    sys.setrecursionlimit(10001)

    INX = 0

    while INX <= 4000:

        F7_1_TIME = Timer(lambda: get_left_sum_7_1(INX)).timeit(number=5)
        F7_2_TIME = Timer(lambda: get_left_sum_7_2(INX)).timeit(number=5)
        F7_3_TIME = Timer(lambda: get_left_sum_7_1_1(INX)).timeit(number=5)

        print(f"""get_left_sum_7_1\t|{INX}\t|{F7_1_TIME}""")
        print(f"""get_left_sum_7_2\t|{INX}\t|{F7_2_TIME}""")
        print(f"""get_left_sum_7_1_1\t|{INX}\t|{F7_3_TIME}""")

        INX += 1000
    sys.setrecursionlimit(RECURSION_LIMIT)

    INX = 1
    while INX <= 99999999999999999999:

        F8 = Timer(lambda: inverted_num_recurs(123456789012345678901234567890)).timeit(number=5)
        F9 = Timer(lambda: inverted_num_series(123456789012345678901234567890)).timeit(number=5)
        F10 = Timer(lambda: inverted_num_list(123456789012345678901234567890)).timeit(number=5)
        print(f"""inverted_num_recurs\t|{123456789012345678901234567890}\t|{F8}""")
        print(f"""inverted_num_series\t|{123456789012345678901234567890}\t|{F9}""")
        print(f"""inverted_num_list\t|{123456789012345678901234567890}\t|{F10}""")

        INX *= 123456712

"""
I.
Функция get_left_sum_7_1 примерно в 3 раза быстрее чем get_left_sum_7_2, т.к. исспользуется цикл.
Функция get_left_sum_7_1_1 примерно в 3 раза быстрее работает чем get_left_sum_7_1, 
вместо цикла исспользуется генератора списка
Сложность всех алгоритмов О(n), отличается только реализация.
Рекурсия медленнее чем цикл, цикл медленнее генератора списка.

II.
Функция inverted_num_recurs примерно в 3 раза быстрее чем inverted_num_series, 
т.к. исспользуется цикл вместо рекурсии.
Функция inverted_num_list примерно в 2 раза быстрее работает чем inverted_num_series, 
вместо цикла исспользуется функции списка.
Сложность всех алгоритмов О(n), отличается только реализация.

get_left_sum_7_1	|0	|6.309999999999649e-05
get_left_sum_7_2	|0	|7.3000000000017495e-06
get_left_sum_7_1_1	|0	|2.0999999999993246e-05
get_left_sum_7_1	|1000	|0.0016560999999999937
get_left_sum_7_2	|1000	|0.008680499999999994
get_left_sum_7_1_1	|1000	|0.0009775999999999951
get_left_sum_7_1	|2000	|0.006930399999999989
get_left_sum_7_2	|2000	|0.026380199999999993
get_left_sum_7_1_1	|2000	|0.002535399999999993
get_left_sum_7_1	|3000	|0.013066899999999992
get_left_sum_7_2	|3000	|0.024155999999999983
get_left_sum_7_1_1	|3000	|0.006429299999999999
get_left_sum_7_1	|4000	|0.00770789999999999
get_left_sum_7_2	|4000	|0.03122039999999998
get_left_sum_7_1_1	|4000	|0.002400299999999994
inverted_num_recurs	|123456789012345678901234567890	|0.00037439999999999696
inverted_num_series	|123456789012345678901234567890	|0.0001290999999999931
inverted_num_list	|123456789012345678901234567890	|5.300000000002525e-05
inverted_num_recurs	|123456789012345678901234567890	|0.000777099999999975
inverted_num_series	|123456789012345678901234567890	|0.0017362999999999962
inverted_num_list	|123456789012345678901234567890	|6.729999999999237e-05
inverted_num_recurs	|123456789012345678901234567890	|0.001257199999999986
inverted_num_series	|123456789012345678901234567890	|0.0002143000000000006
inverted_num_list	|123456789012345678901234567890	|8.599999999997499e-05
inverted_num_recurs	|123456789012345678901234567890	|0.0007448999999999928
inverted_num_series	|123456789012345678901234567890	|0.0001838999999999591
inverted_num_list	|123456789012345678901234567890	|6.359999999999699e-05
inverted_num_recurs	|123456789012345678901234567890	|0.0006297000000000108
inverted_num_series	|123456789012345678901234567890	|0.00013169999999995685
inverted_num_list	|123456789012345678901234567890	|4.070000000000462e-05
inverted_num_recurs	|123456789012345678901234567890	|0.000516400000000028
inverted_num_series	|123456789012345678901234567890	|0.00012860000000003424
inverted_num_list	|123456789012345678901234567890	|5.969999999999587e-05
inverted_num_recurs	|123456789012345678901234567890	|0.0004192999999999558
inverted_num_series	|123456789012345678901234567890	|0.00022280000000002298
inverted_num_list	|123456789012345678901234567890	|4.1100000000016124e-05
inverted_num_recurs	|123456789012345678901234567890	|0.00043080000000000895
inverted_num_series	|123456789012345678901234567890	|0.00012929999999999886
inverted_num_list	|123456789012345678901234567890	|3.6399999999991994e-05
inverted_num_recurs	|123456789012345678901234567890	|0.00042680000000000495
inverted_num_series	|123456789012345678901234567890	|0.00012879999999998448
inverted_num_list	|123456789012345678901234567890	|3.56000000000245e-05
"""
