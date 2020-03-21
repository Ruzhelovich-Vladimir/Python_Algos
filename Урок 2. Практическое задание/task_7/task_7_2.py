"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

import sys


def get_left_sum(n_value, elem=1, summa=0):
    """
    Функция расчёта левой части уравления
    :param n_value:
    :return:
    """

    if elem <= n_value:
        summa += elem
        elem += 1
        return get_left_sum(n_value, elem, summa)
    return summa


if __name__ == "__main__":

    print("Проверка уровнения: 1+2+...+n = n(n+1)/2")
    N = int(input("Введите число n:"))
    SAVE_LIMIT_RECURS = sys.getrecursionlimit()
    print(SAVE_LIMIT_RECURS)
    sys.setrecursionlimit(N + 10)
    SAVE_LIMIT_RECURS1 = sys.getrecursionlimit()
    print(SAVE_LIMIT_RECURS1)
    # Увеличивая ограничение рекурсивного вызова я всё равно столкунулся
    # с перепонения стека, на досуге почитаю по данному вопросу.

    print("Уравнение верное" if get_left_sum(N) == (
        N * (N + 1) / 2) else "Уравнение не верное")

    sys.setrecursionlimit(SAVE_LIMIT_RECURS)
