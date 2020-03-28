"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

# Наполнение массива
from random import randint
LEN_ARRAY = 100
MIN = -10
MAX = 10
ARRAY = [randint(MIN, MAX) for cont in range(LEN_ARRAY)]
############################################################
print(
    f"""Чаще всего встречается число {max(ARRAY, key=ARRAY.count)} в массиве\n {ARRAY}""")
