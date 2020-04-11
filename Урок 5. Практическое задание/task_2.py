"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque


class HexOperation1:
    """
    Класс для выполнения арифметических операций над 16-ми числами через коллекцию
    """

    def __init__(self, hexlist):
        """
        :param hexstr:
        """
        self.list_hex = hexlist

    def get_int(self, hex_value):
        """
        Получиение  сисла из очереди deque в 16-ной системе исчисления
        :param deque_hex: 16-ное число впредставлена при помощи deque
        :return:
        """
        result = 0
        degree = 1  # разряд 16 ** 0

        while hex_value:
            # переводим число в десятичное исчисление
            elem = hex_value.pop()
            result += int(elem, 16) * degree
            degree *= 16

        return result

    def get_hex(self, dec):
        """ Получение из десятичного числа шеснадцетиричное"""
        division = (dec % 16)
        digits = "0123456789ABCDEF"
        rest = dec // 16
        if rest == 0:
            return digits[division]
        return self.get_hex(rest) + digits[division]

    def __add__(self, other):
        """Сложение"""

        # Преобразуем список в очередь для первого числа
        deque1 = deque(self.list_hex)
        # Преобразуем список в очередь для второго числа
        deque2 = deque(other.list_hex)

        return list(
            self.get_hex(
                self.get_int(deque1) +
                self.get_int(deque2)).upper())

    def __mul__(self, other):
        """Умножение"""
        # Преобразуем список в очередь для первого числа
        deque1 = deque(self.list_hex)
        # Преобразуем список в очередь для второго числа
        deque2 = deque(other.list_hex)

        return list(
            self.get_hex(
                self.get_int(deque1) *
                self.get_int(deque2)).upper())


class HexOperation2(HexOperation1):
    """
    Класс для выполнения арифметических операций над 16-ми числами не через коллекцию
    """

    def get_int(self, hex_value):
        """
        Получиение  дясятичного числа
        :param deque_hex: 16-ное число при помощи списка
        :return:
        """
        result = 0
        degree = 1  # разряд 16 ** 0
        inx = len(hex_value) - 1

        while inx >= 0:
            result += int(hex_value[inx], 16) * degree
            degree *= 16
            inx -= 1

        return result

    def __add__(self, other):
        """Сложение"""

        # Преобразуем список в очередь для первого числа
        list1 = self.list_hex
        # Преобразуем список в очередь для второго числа
        list2 = other.list_hex

        return list(
            self.get_hex(
                self.get_int(list1) +
                self.get_int(list2)).upper())

    def __mul__(self, other):
        """Умножение"""
        # Преобразуем список в очередь для первого числа
        list1 = self.list_hex
        # Преобразуем список в очередь для второго числа
        list2 = other.list_hex

        return list(
            self.get_hex(
                self.get_int(list1) *
                self.get_int(list2)).upper())


#HEX_1 = list('12345abcdf')
#HEX_2 = list('98765fdc')
HEX_1, HEX_2 = input(
    "Введите два шеснадцетиричных числа разделёнными пробелом (ab06 56ab):").split(" ")

HEX_1 = list(HEX_1)
HEX_2 = list(HEX_2)

print(f"Сложение: {HEX_1} + {HEX_2}")
print(
    f"При помощи модуля collections:{HexOperation1(HEX_1) + HexOperation1(HEX_2)}")
print(
    f"При помощи списка:{HexOperation2(HEX_1) + HexOperation2(HEX_2)}")
print(
    f"Одной строкой:{list(hex(int(''.join(HEX_1),16) + int(''.join(HEX_2),16))[2:])}")
print(f"Умножение: {HEX_1} * {HEX_2}")
print(
    f"При помощи модуля collections:{HexOperation1(HEX_1) * HexOperation1(HEX_2)}")
print(
    f"Одной строкой:{HexOperation2(HEX_1) * HexOperation2(HEX_2)}")
print(
    f"Одной строкой:{list(hex(int(''.join(HEX_1),16) * int(''.join(HEX_2),16))[2:])}")

"""
Введите два шеснадцетиричных числа разделёнными пробелом (ab06 56ab):aaaa aaaaaa
Сложение: ['a', 'a', 'a', 'a'] + ['a', 'a', 'a', 'a', 'a', 'a']
При помощи модуля collections:['A', 'B', '5', '5', '5', '4']
При помощи списка:['A', 'B', '5', '5', '5', '4']
Одной строкой:['a', 'b', '5', '5', '5', '4']
Умножение: ['a', 'a', 'a', 'a'] * ['a', 'a', 'a', 'a', 'a', 'a']
При помощи модуля collections:['7', '1', 'C', '6', 'A', 'A', '3', '8', 'E', '4']
Одной строкой:['7', '1', 'C', '6', 'A', 'A', '3', '8', 'E', '4']
Одной строкой:['7', '1', 'c', '6', 'a', 'a', '3', '8', 'e', '4']
"""
