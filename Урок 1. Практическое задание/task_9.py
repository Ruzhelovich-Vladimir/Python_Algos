"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
if __name__ == "__main__":

    print(f"{'='*10} Демонстрация решения 9-й задачи")
    print("Введите 3 разных числа:")

    try:
        VALUE_1 = float(input("1-е число:"))
        VALUE_2 = float(input("2-е число:"))
        VALUE_3 = float(input("3-е число:"))
    except ValueError:
        raise ValueError("Ошибка.Введенный параметр не является числом.")

    if VALUE_1 == VALUE_2 or VALUE_1 == VALUE_3 or VALUE_2 == VALUE_3:
        raise ValueError("Ошибка.Введенный равные числа.")

    if VALUE_1 < VALUE_2 < VALUE_3 or VALUE_3 < VALUE_2 < VALUE_1:
        print(f"Средним числом является:{VALUE_2}")
    elif VALUE_1 < VALUE_3 < VALUE_2 or VALUE_2 < VALUE_3 < VALUE_1:
        print(f"Средним числом является:{VALUE_3}")
    elif VALUE_2 < VALUE_1 < VALUE_3 or VALUE_3 < VALUE_1 < VALUE_2:
        print(f"Средним числом является:{VALUE_1}")
