"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

# ИСПОЛЬЗУЮ ПЕРВЫЙ ПРИМЕР РЕАЛИЗАЦИИ, СЧИТАЮ ДЛЯ ОРГАНИЗАЦИИ ДЕРЕВА
# НЕ ОБЯЗАТЕЛЬНО ПОЛЬЗОВАТЬСЯ КЛАССАМИ, КЛАССЫ, КАК МНЕ КАЖЕТСЯ, ТРЕБУЕТСЯ
# ИСПОЛЬЗОВАТЬ ДЛЯ ОБЪЕКТОВ С МЕТОДАМИ

from collections import Counter, deque


def haffman_tree(str_param):
    """
    Постраение дерева Хаффмана
    :param str_param:
    :return: словарь-дерево
    """
    # Подсчитываем кол-во всех символов в строке
    count_chars = Counter(str_param)
    # Сортируем список сиволов не по убыванию повторений,
    # преобразуя данный список в очередь
    sorted_chars = deque(sorted(count_chars.items(), key=lambda item: item[1]))

    # Если строка состоит из более одного повторяющего символа
    if len(sorted_chars) != 1:
        # пока очередь не пустая, строим дерево
        while len(sorted_chars) > 1:
            # объединяет два крайних левых элемента,
            # расчитываем значение вхождения символов-потомков в строке
            includes_count = sorted_chars[0][1] + sorted_chars[1][1]
            # 2 крайних левых элементов, объединяем в словарь,
            # у левого ключ = 0, у правго ключ = 1
            comb = {0: sorted_chars.popleft()[0],
                    1: sorted_chars.popleft()[0]}
            # Ищем место для ставки объединенного элемента
            # оно должно не нарушить не убывающую последовательность
            for inx, _count in enumerate(sorted_chars):
                if includes_count <= _count[1]:
                    # Вставляем объединенный элемент
                    sorted_chars.insert(inx, (comb, includes_count))
                    break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла
                sorted_chars.append((comb, includes_count))
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        includes_count = sorted_chars[0][1]
        comb = {0: sorted_chars.popleft()[0], 1: None}
        sorted_chars.append((comb, includes_count))
    # словарь - дерево
    return sorted_chars[0][0]


CODE_TABLE = dict()


def haffman_code(tree, path=''):
    """
    Преобразования дерева в словарь
    :param tree:
    :param path:
    :return:
    """
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        CODE_TABLE[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


# строка для кодирования
USR_STR = "Алгоритмы - полезный курс"

haffman_code(haffman_tree(USR_STR))
print(f"Таблица Хаффмана: {CODE_TABLE}")

print(f"Исходная строка: {USR_STR}")
print(f"Закодированная строка по Хаффману: ")
for i in USR_STR:
    print(CODE_TABLE[i], end=' ')
print()
