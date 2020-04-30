"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""

from hashlib import sha1
# Больше понравился алгоритм через множество


USR_STR = input("Введите строку из маленьких латинских букв: ")
RES_SET = set()  # Будет собираться уникальные подстроки

LEN_STR = len(USR_STR)  # Кл-во элементов в строке
print(f"Строка: {USR_STR}", end="\n")
print(f"подстроки:", end="\n\n")

# Находим всевозможные подстроки строки
for INX_1 in range(LEN_STR):  # Индекс первого элемента
    # Если первый проход, то пропускаем построку равную строке,
    # убирая последний символ
    N = LEN_STR - 1 if INX_1 == 0 else LEN_STR
    # Добавляем все хеш суммы подстрок с INX_1 по INX_2 в множество RES_SET
    for INX_2 in range(N, INX_1, -1):  # Индекс второго элемента
        print(USR_STR[INX_1:INX_2])
        RES_SET.add(sha1(USR_STR[INX_1:INX_2].encode('utf-8')).hexdigest())

print(f"\nИтог: {len(RES_SET)} подстрок")

"""
Результаты:
Введите строку из маленьких латинских букв: papa
строка: papa
pap
pa
p
apa
ap
a
pa
p
a
Итог: 6 уникальных подстрок
"""
