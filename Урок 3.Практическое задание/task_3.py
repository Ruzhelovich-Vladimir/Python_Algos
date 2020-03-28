"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

# Решение в лоб, ничего больше не удалось придумать,
# линейный перебор поиска максимально и мимального числа.

from random import randint
LEN_ARRAY = 10000
MIN = -100
MAX = 100
#ARRAY = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
ARRAY = [randint(MIN, MAX) for cont in range(LEN_ARRAY)]

ARRAY_RESULT = ARRAY.copy()

MIN_INX = MAX_INX = 0
MIN_ELEM = MAX_ELEM = ARRAY[MAX_INX]

for INX, ELEM in enumerate(ARRAY):
    if MAX_ELEM < ELEM:
        MAX_INX, MAX_ELEM = INX, ELEM
    if MIN_ELEM > ELEM:
        MIN_INX, MIN_ELEM = INX, ELEM

ARRAY_RESULT[MAX_INX] = MIN_ELEM
ARRAY_RESULT[MIN_INX] = MAX_ELEM

if MIN_INX == MAX_INX:
    print("Минимальное и максимальное значение совподает")
else:
    print(f"""\
В данном массиве чисел максимальное число   {MAX_ELEM} стоит на
{MAX_INX} позиции, а минимальное число  {MIN_ELEM} стоит на   {MIN_INX}  позиции
Заменяем их
{ARRAY}
В данном массиве чисел максимальное число   {MAX_ELEM} стоит на
{MIN_INX} позиции, а минимальное число  {MIN_ELEM} стоит на    {MAX_INX} позиции
{ARRAY_RESULT}
    """)
