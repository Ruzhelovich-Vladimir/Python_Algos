"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randint

COUNT_X = int(input("Задайте количество строк в матрице: "))
COUNT_Y = int(input("Задайте количество столбцов в матрице: "))
# Генерируем основную матрицу
ARRAY = [[randint(0, 100) for J in range(COUNT_X)]
         for I in range(COUNT_Y)]    # генерация двумерного списка
# Генерируем странспонируемую матрицу
ARRAY_TRANS = [[ARRAY[J][I] for J in range(COUNT_Y)]
               for I in range(COUNT_X)]
# Генерирую массив из минимальных значений по строкам из транспонированной
# матрице
MIN_COLOM_ARRAY = [min(ARRAY_TRANS[I]) for I, _ in enumerate(ARRAY_TRANS)]
# Вывод на экран таблицы
for row in ARRAY:
    str_row = ""
    for elem in row:
        str_row += str(elem) + "\t"
    print(str_row)
print(f"""
{MIN_COLOM_ARRAY} минимальные значения по столбцам
Максимальное среди них = {max(MIN_COLOM_ARRAY)}
""")
