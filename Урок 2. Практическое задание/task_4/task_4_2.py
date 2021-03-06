"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def range_sum(count, start=1, step=1, summ=0):
    """
    Основная функция
    """
    if count < 1:
        return summ
    else:
        summ += start       # сумма
        start *= step       # элемент
        count -= 1          # Обратный счётчик рекурсии
        return range_sum(count, start, step, summ)


if __name__ == "__main__":

    elem_num = int(input("Введите количество элементов ряда: "))
    if elem_num < 1:
        print("Ошибка. Колличество должно быть больше нуля")
    else:
        print(
            f"Количество элементов - {elem_num}, их сумма - {range_sum(elem_num,1,-0.5)}")
