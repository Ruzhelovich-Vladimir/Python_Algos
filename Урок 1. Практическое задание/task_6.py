"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

if __name__ == "__main__":

    print(f"{'=' * 10} Демонстрация решения 6-й задачи")
    PLACE_POSITION = input("Введите номер буквы в латинском алфавите:")

    try:
        PLACE_POSITION = int(PLACE_POSITION)
    except ValueError:
        raise ValueError("Ошибка. Параметр не являеся числом")
    if PLACE_POSITION not in range(1, 26):
        raise ValueError(
            "Ошибка. Параметр не является позицией в латинском алфавите")

    print(
        f"Позиция {PLACE_POSITION} соотвествует букве - '{chr(ord('A')+PLACE_POSITION-1)}'")
