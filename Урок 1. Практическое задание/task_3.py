"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""


def input_coordinates(msg=""):
    """
    Запрашивает у пользователя координаты точки, не исспользуя массив (с массивом было элегантнее).
    :param msg: строка для уточгения для пользователя
    :return:
    возвразает два числа X,Y или None, None
    """
    while True:

        usr_txt = input(f"Введите координаты {msg} 'x,y' или 'q': ").strip()
        if usr_txt == 'q':
            return None, None

        if usr_txt.count(',') == 1:
            index_separator = usr_txt.find(',')
            x_str = usr_txt[:index_separator]
            y_str = usr_txt[index_separator + 1:]
            try:
                x_float = float(x_str)
                y_float = float(y_str)
            except ValueError:
                print('Ошибка.Не является числом одно из значений')
            else:
                return x_float, y_float
        else:
            print('Ошибка.Список не из двух чисел')


if __name__ == "__main__":

    X1, Y1 = input_coordinates('1-й точки')
    X2, Y2 = input_coordinates('2-й точки')

    if None not in (X1, X2):
        B = X2 * Y1 - X1 * Y2
        print(
            f"y = {(Y2-Y1)/(X2-X1)}x{(' + ' if B>0 else ' - ')}{abs(B/(X2-X1))}")
