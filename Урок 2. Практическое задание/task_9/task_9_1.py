"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

if __name__ == "__main__":

    COUNT = int(input("Введите количество чисел: "))

    I = 1
    COUNT_NUMBER = 0
    NUM_MAX = None
    SUM_MAX = None

    while I <= COUNT:
        VALUE_SAVE = VALUE = int(input(f"Введите очередное число: "))
        SUMMA = 0
        while VALUE > 0:
            SUMMA += VALUE % 10
            VALUE = VALUE // 10
        if SUM_MAX is None or SUM_MAX < SUMMA:
            SUM_MAX = SUMMA
            NUM_MAX = VALUE_SAVE
        I += 1

    print(
        f"Наибольшее число по сумме цифр: {NUM_MAX}, сумма его цифр: {SUM_MAX}")
