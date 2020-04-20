"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile
#from sys import getrefcount

@profile
def lesson3_task7_v1():
    """
    Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться.

    Пример:
    Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
    Наименьший элемент: -86, встречается в этом массиве 1 раз
    Второй наименьший элемент: -73
    """

    # Наполнение массива
    from random import randint

    array_len = 100000
    min_value = -array_len
    max_value = array_len
    array = [randint(min_value, max_value) for cont in range(array_len)]

    # РЕШЕНИЕ ВАРИАТ №1 поиска минимальное числа
    tmp_array = array.copy()  # КОПИРУЕМ СПИСОК
    min_elem_1 = min(tmp_array)  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    tmp_array.remove(min_elem_1)  # УДАЛЯЕМ ИЗ ВРЕМЕННОГО СПИСКА МИНИМАЛЬНЫЙ ЭЛЕМЕНТ
    min_elem_2 = min(tmp_array)  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ

    del tmp_array
    print(f"""
    Исходный массив: {array}
    Наименьший элемент: {min_elem_1}, встречается в этом массиве {array.count(min_elem_1)} раз
    Второй наименьший элемент: {min_elem_2}
    """)

    # РЕШЕНИЕ ВАРИАТ №2 - сортировка
    tmp_array = array.copy()  # КОПИРУЕМ СПИСОК И СОРТИРУЕМ ЕГО

    tmp_array.sort()

    min_elem_1 = tmp_array[0]  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    min_elem_2 = tmp_array[1]  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    del tmp_array
    print(f"""
    Исходный массив: {array}
    Наименьший элемент: {min_elem_1}, встречается в этом массиве {array.count(min_elem_2)} раз
    Второй наименьший элемент: {min_elem_2}
    """)
    del array

@profile
def lesson3_task7_v2():
    """
    Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться.

    Пример:
    Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
    Наименьший элемент: -86, встречается в этом массиве 1 раз
    Второй наименьший элемент: -73
    """

    # Наполнение массива
    from random import randint

    array_len = 100000
    min_value = -array_len
    max_value = array_len
    array = (randint(min_value, max_value) for _ in range(array_len))

    min_elem_1 = min_elem_2 = array_len + 1
    cont_elem_1 = cont_elem_2 = 0
    print("Исходный массив: ", end="[")
    for elem in array:
        print(elem, end=", ")
        if elem < min_elem_1:
            min_elem_1 = elem
            cont_elem_1 += 1
        if min_elem_1 < elem < min_elem_2:
            min_elem_2 = elem
            cont_elem_2 += 1

    print(f"""]
    Наименьший элемент: {min_elem_1}, встречается в этом массиве {cont_elem_1} раз
    Второй наименьший элемент: {min_elem_2}, встречается в этом массиве {cont_elem_2} раз
    """)
    del array


"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

"""НАПИСАЛ 3 АЛГОРИТМА, АНАЛИЗ НИЖЕ"""

@profile
def lesson4_task1_get_prime_number_v2(i):
    """
    нахождения i-го по счёту простого числа
    без использования «Решета Эратосфена, дорабатываю get_prime_number_v1 чтобы
    исключить лишние делители, т.е делим только на простые числа
    :param i:
    :return: i-е простое число
    """

    prime_numbers = [2]        # Начальное состояние массива простых чисел
    current_elem = 2           # Начальное значение 1-го простого числа
    while len(prime_numbers) < i:
        current_elem += 1
        prime_number = True
        for divisor in prime_numbers:
            if current_elem % divisor == 0:
                prime_number = False
                break
            # переберать надо только числа, не превосходящие корня из искомого
            if divisor > (int(current_elem ** 0.5) + 1):
                break
        if prime_number:
            prime_numbers.append(current_elem)
            #print(len(prime_numbers), current_elem)

    return prime_numbers[i - 1]

@profile
def lesson4_task1_get_prime_number_v3(i, range_prime_number):
    """
    нахождения i-го по счёту простого числа
    с использованиеи «Решета Эратосфена
    :param i: i
    :return:
    """

    result = 2

    # Массив поиска
    arr = [j for j in range(range_prime_number)]

    inx_i = 0

    for inx_j in range(2, len(arr)):
        # Если значение ячейки до этого не было обнулено - это простое число
        if arr[inx_j] != 0:
            result = inx_j
            inx_i += 1
            if inx_i == i:
                break
            # первое кратное ему будет в два раза больше
            for inx_j1 in range(inx_j * 2, len(arr), inx_j):
                arr[inx_j1] = 0
    return result

@profile
def lesson4_task1_get_prime_number_v4(i, range_prime_number):
    """
    нахождения i-го по счёту простого числа
    с использованиеи «Решета Эратосфена
    :param i: i
    :return:
    """

    result = 2

    arr = [] #Список не простых чисел

    inx_i = 0

    for inx_j in range(2, range_prime_number):
        # Если значение ячейки до этого не было обнулено - это простое число
        if arr.count(inx_j) == 0:
            result = inx_j
            inx_i += 1
            if inx_i == i:
                break
            # первое кратное ему будет в два раза больше
            for inx_j1 in range(inx_j * 2, range_prime_number, inx_j):
                arr.append(inx_j1)
    return result


##########################################################################
# Блок запуска и анализа
##########################################################################

#lesson3_task7_v1()
'''
Windows10 x64, Python 8 x32

Задача была решена двумя способоми, значительные исспользование памяти наблюдаются на больших 
объемах данных только на генерации списка - 36 строка, что логично как мне кажется
15.4 MiB - 13.3 MiB = 2.1 MiB 

Алгоритм №1 использует 1.1Mib:
    * 0.7MiB - печать большого списка (43 строка)
    * 0.3MiB - копирование с большое списка (39 строка)
Алгоритм №2 использует 1.3Mib:
    * 0.7MiB - печать большого списка (56 строка)
    * 0.3MiB - копирование с большое списка (51 строка)
    * 0.2MiB - сортировка списка (52 строка)

Line #    Mem usage    Increment   Line Contents
================================================
    18     13.2 MiB     13.2 MiB   @profile
    19                             def lesson3_task7():
    20                                 """
    21                                 Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
    22                                 Они могут быть как равны между собой (оба являться минимальными), так и различаться.
    23                             
    24                                 Пример:
    25                                 Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
    26                                 Наименьший элемент: -86, встречается в этом массиве 1 раз
    27                                 Второй наименьший элемент: -73
    28                                 """
    29                             
    30                                 # Наполнение массива
    31     13.3 MiB      0.1 MiB       from random import randint
    32                             
    33     13.3 MiB      0.0 MiB       array_len = 100000
    34     13.3 MiB      0.0 MiB       min_value = -array_len
    35     13.3 MiB      0.0 MiB       max_value = array_len
    36     15.4 MiB      0.2 MiB       array = [randint(min_value, max_value) for cont in range(array_len)]
    37                             
    38                                 # РЕШЕНИЕ ВАРИАТ №1 поиска минимальное числа
    39     15.8 MiB      0.4 MiB       tmp_array = array.copy()  # КОПИРУЕМ СПИСОК
    40     15.8 MiB      0.0 MiB       min_elem_1 = min(tmp_array)  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    41     15.8 MiB      0.0 MiB       tmp_array.remove(min_elem_1)  # УДАЛЯЕМ ИЗ ВРЕМЕННОГО СПИСКА МИНИМАЛЬНЫЙ ЭЛЕМЕНТ
    42     15.8 MiB      0.0 MiB       min_elem_2 = min(tmp_array)  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    43     16.5 MiB      0.7 MiB       print(f"""
    44     15.8 MiB      0.0 MiB       Исходный массив: {array}
    45     16.5 MiB      0.0 MiB       Наименьший элемент: {min_elem_1}, встречается в этом массиве {array.count(min_elem_1)} раз
    46     16.5 MiB      0.0 MiB       Второй наименьший элемент: {min_elem_2}
    47                                 """)
    48     15.2 MiB      0.0 MiB       del tmp_array
    49                             
    50                                 # РЕШЕНИЕ ВАРИАТ №2 - сортировка
    51     15.6 MiB      0.4 MiB       tmp_array = array.copy()  # КОПИРУЕМ СПИСОК И СОРТИРУЕМ ЕГО
    52     15.8 MiB      0.2 MiB       tmp_array.sort()
    53     15.8 MiB      0.0 MiB       min_elem_1 = tmp_array[0]  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    54     15.8 MiB      0.0 MiB       min_elem_2 = tmp_array[1]  # ИЩЕМ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ
    55     16.5 MiB      0.7 MiB       print(f"""
    56     15.8 MiB      0.0 MiB       Исходный массив: {array}
    57     16.5 MiB      0.0 MiB       Наименьший элемент: {min_elem_1}, встречается в этом массиве {array.count(min_elem_2)} раз
    58     16.5 MiB      0.0 MiB       Второй наименьший элемент: {min_elem_2}
    59                                 """)
    60                             
    61     15.2 MiB      0.0 MiB       del array
    
'''
#lesson3_task7_v2()

'''
После перевода на генератор кортежей, инкримента памяти практически нет, сам генератор кортежа сейчас
занимает около 0.1MiB вместо 2.1MiB, также меньше исспользуется памяти на вывод массива на экран, т.к.
проиходит перебор

Line #    Mem usage    Increment   Line Contents
================================================
    67     13.4 MiB     13.4 MiB   @profile
    68                             def lesson3_task7_v2():
    69                                 """
    70                                 Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
    71                                 Они могут быть как равны между собой (оба являться минимальными), так и различаться.
    72                             
    73                                 Пример:
    74                                 Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
    75                                 Наименьший элемент: -86, встречается в этом массиве 1 раз
    76                                 Второй наименьший элемент: -73
    77                                 """
    78                             
    79                                 # Наполнение массива
    80     13.4 MiB      0.1 MiB       from random import randint
    81                             
    82     13.4 MiB      0.0 MiB       array_len = 100000
    83     13.4 MiB      0.0 MiB       min_value = -array_len
    84     13.4 MiB      0.0 MiB       max_value = array_len
    85     13.5 MiB      0.0 MiB       array = (randint(min_value, max_value) for _ in range(array_len))
    86                             
    87     13.4 MiB      0.0 MiB       min_elem_1 = min_elem_2 = array_len + 1
    88     13.4 MiB      0.0 MiB       cont_elem_1 = cont_elem_2 = 0
    89     13.4 MiB      0.0 MiB       print("Исходный массив: ", end="[")
    90     13.5 MiB      0.0 MiB       for elem in array:
    91     13.5 MiB      0.0 MiB           print(elem, end=", ")
    92     13.5 MiB      0.0 MiB           if elem < min_elem_1:
    93     13.4 MiB      0.0 MiB               min_elem_1 = elem
    94     13.4 MiB      0.0 MiB               cont_elem_1 += 1
    95     13.5 MiB      0.0 MiB           if min_elem_1 < elem < min_elem_2:
    96     13.4 MiB      0.0 MiB               min_elem_2 = elem
    97     13.4 MiB      0.0 MiB               cont_elem_2 += 1
    98                             
    99     13.5 MiB      0.0 MiB       print(f"""]
   100     13.5 MiB      0.0 MiB       Наименьший элемент: {min_elem_1}, встречается в этом массиве {cont_elem_1} раз
   101     13.5 MiB      0.0 MiB       Второй наименьший элемент: {min_elem_2}, встречается в этом массиве {cont_elem_2} раз
   102                                 """)
   103     13.5 MiB      0.0 MiB       del array
   '''

#ITEMS = 100
#print(lesson4_task1_get_prime_number_v2(ITEMS))

'''
Во второй версии без исспользования "Решета Эратосфена", нет потери памяти, т.к. не формируется список,
формируется только список простых чисел, который используется для определяния простых чисел.
Этот алгоритм со создаёт большоего объёма информации, но он медленне на больших значениях.
   
Line #    Mem usage    Increment   Line Contents
================================================
   123     13.4 MiB     13.4 MiB   @profile
   124                             def lesson4_task1_get_prime_number_v2(i):
   125                                 """
   126                                 нахождения i-го по счёту простого числа
   127                                 без использования «Решета Эратосфена, дорабатываю get_prime_number_v1 чтобы
   128                                 исключить лишние делители, т.е делим только на простые числа
   129                                 :param i:
   130                                 :return: i-е простое число
   131                                 """
   132                             
   133     13.4 MiB      0.0 MiB       prime_numbers = [2]        # Начальное состояние массива простых чисел
   134     13.4 MiB      0.0 MiB       current_elem = 2           # Начальное значение 1-го простого числа
   135     13.4 MiB      0.0 MiB       while len(prime_numbers) < i:
   136     13.4 MiB      0.0 MiB           current_elem += 1
   137     13.4 MiB      0.0 MiB           prime_number = True
   138     13.4 MiB      0.0 MiB           for divisor in prime_numbers:
   139     13.4 MiB      0.0 MiB               if current_elem % divisor == 0:
   140     13.4 MiB      0.0 MiB                   prime_number = False
   141     13.4 MiB      0.0 MiB                   break
   142                                         # переберать надо только числа, не превосходящие корня из искомого
   143     13.4 MiB      0.0 MiB               if divisor > (int(current_elem ** 0.5) + 1):
   144     13.4 MiB      0.0 MiB                   break
   145     13.4 MiB      0.0 MiB           if prime_number:
   146     13.4 MiB      0.0 MiB               prime_numbers.append(current_elem)
   147                                         #print(len(prime_numbers), current_elem)
   148                             
   149     13.4 MiB      0.0 MiB       return prime_numbers[i - 1]
'''

#ITEMS = 1000
#print(lesson4_task1_get_prime_number_v3(ITEMS, ITEMS ** 2))

'''
В данном алгоритме наблюдается большие потери памяти из-за исспользования большого 
генератора списка, к сожалени нельзя исспользовать генераторкортжей, т.к. требуется,
изменять элементы массива, потери состояляют 19.2 MiB (161 строка).

Line #    Mem usage    Increment   Line Contents
================================================
   151     13.4 MiB     13.4 MiB   @profile
   152                             def lesson4_task1_get_prime_number_v3(i, range_prime_number):
   153                                 """
   154                                 нахождения i-го по счёту простого числа
   155                                 с использованиеи «Решета Эратосфена
   156                                 :param i: i
   157                                 :return:
   158                                 """
   159                             
   160     13.4 MiB      0.0 MiB       result = 2
   161                             
   162                                 # Массив поиска
   163     32.6 MiB      0.4 MiB       arr = [j for j in range(range_prime_number)]
   164                             
   165     32.6 MiB      0.0 MiB       inx_i = 0
   166                             
   167     32.6 MiB      0.0 MiB       for inx_j in range(2, len(arr)):
   168                                     # Если значение ячейки до этого не было обнулено - это простое число
   169     32.6 MiB      0.0 MiB           if arr[inx_j] != 0:
   170     32.6 MiB      0.0 MiB               result = inx_j
   171     32.6 MiB      0.0 MiB               inx_i += 1
   172     32.6 MiB      0.0 MiB               if inx_i == i:
   173     32.5 MiB      0.0 MiB                   break
   174                                         # первое кратное ему будет в два раза больше
   175     32.6 MiB      0.0 MiB               for inx_j1 in range(inx_j * 2, len(arr), inx_j):
   176     32.6 MiB      0.0 MiB                   arr[inx_j1] = 0
   177     32.5 MiB      0.0 MiB       return result
'''

#ITEMS = 1000
#print(lesson4_task1_get_prime_number_v4(ITEMS, ITEMS ** 2))

'''
Попытался немного модернизировать алгоритм, не создавая сразу списка, 
а по ходу добавлять не простые чисола в пустой список, идея мне показалась интересная, но
потери памяти составили 47.1MiB, скорее всего из-за отсудствия генератора списка.

Line #    Mem usage    Increment   Line Contents
================================================
   179     13.9 MiB     13.9 MiB   @profile
   180                             def lesson4_task1_get_prime_number_v4(i, range_prime_number):
   181                                 """
   182                                 нахождения i-го по счёту простого числа
   183                                 с использованиеи «Решета Эратосфена
   184                                 :param i: i
   185                                 :return:
   186                                 """
   187                             
   188     13.9 MiB      0.0 MiB       result = 2
   189                             
   190     13.9 MiB      0.0 MiB       arr = [] #Список не простых чисел
   191                             
   192     13.9 MiB      0.0 MiB       inx_i = 0
   193                             
   194     61.0 MiB      0.0 MiB       for inx_j in range(2, range_prime_number):
   195                                     # Если значение ячейки до этого не было обнулено - это простое число
   196     61.0 MiB      0.0 MiB           if arr.count(inx_j) == 0:
   197     61.0 MiB      0.0 MiB               result = inx_j
   198     61.0 MiB      0.0 MiB               inx_i += 1
   199     61.0 MiB      0.0 MiB               if inx_i == i:
   200     57.8 MiB      0.0 MiB                   break
   201                                         # первое кратное ему будет в два раза больше
   202     61.0 MiB      0.0 MiB               for inx_j1 in range(inx_j * 2, range_prime_number, inx_j):
   203     61.0 MiB      0.4 MiB                   arr.append(inx_j1)
   204     57.8 MiB      0.0 MiB       return result

'''
