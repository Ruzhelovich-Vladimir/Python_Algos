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

def get_prime_number_v1(i):
    """
    нахождения i-го по счёту простого числа
    без использования «Решета Эратосфена
    :param i:
    :return: i-е простое число
    """
    current_elem = result = 2  # Начальное значение  - 1-е простое число
    inx_i = 1                  # Счётчик i-го простого числа
    while inx_i < i:
        current_elem += 1
        divisor = 2
        while current_elem % divisor != 0 and divisor < current_elem:
            divisor += 1
        if divisor == current_elem:
            inx_i += 1
            result = current_elem
            # print(inx_i,result)

    return result


def get_prime_number_v2(i):
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


def get_prime_number_v3(i, range_prime_number):
    """
    нахождения i-го по счёту простого числа
    с использованиеи «Решета Эратосфена
    :param i: i
    :return:
    """

    result = 2

    # Массив поиска
    # Если я не ошибаюсь, массив должен быть не больше i ** 2
    arr = [j for j in range(range_prime_number)]
    # Использую бинарную строку, но всеравно индекс вышел за границу допустмого значения
    # bytearray(b"\1" * int(i ** 2)))

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


if __name__ == '__main__':
    from timeit import Timer

    INX = 10
    RANGE_PRIME_NUMBER = 160000 # Верхняя граниза простого числа для 10000
    F1_TIME = F2_TIME = F3_TIME = 0  # Начальное время работы каждой функции

    # Измеряю с шагом 100 3 функции
    while INX <= 100000:
        # Если предыдущее значение хуже минимальное значения в 50 раз
        # пропускаем
        if min(F1_TIME, F2_TIME, F3_TIME) * 50 >= F1_TIME:
            F1_TIME = Timer(
                (lambda: get_prime_number_v1(INX))).timeit(number=3) * 1000
            print(f"""get_prime_number_v1|{INX}|{F1_TIME}""")
        else:
            F1_TIME = 9999999999  # Бесконечность
        # Если предыдущее значение хуже минимальное значения в 50 раз
        # пропускаем
        if min(F1_TIME, F2_TIME, F3_TIME) * 50 >= F2_TIME:
            F2_TIME = Timer(
                (lambda: get_prime_number_v2(INX))).timeit(number=3) * 1000
            print(f"""get_prime_number_v2|{INX}|{F2_TIME}""")
        else:
            F2_TIME = 9999999999  # Бесконечность
        # Если предыдущее значение хуже минимальное значения в 50 раз
        # пропускаем
        if min(F1_TIME, F2_TIME, F3_TIME) * 50 >= F3_TIME:
            F3_TIME = Timer(
                (lambda: get_prime_number_v3(INX, RANGE_PRIME_NUMBER))).timeit(number=3) * 1000
            print(f"""get_prime_number_v3|{INX}|{F3_TIME}""")
        else:
            F3_TIME = 9999999999  # Бесконечность
        INX += 100 if INX % 50 == 0 else 90

'''
1. get_prime_number_v1: Функция показала лучший результат для параметра (10),
сложность функция по перебору значений и поиска простого = О(N ** 2)

2. get_prime_number_v2: Функция по созданию списка протых чисел и исспользование
данного списка для поиска следующего простого числа показала лучние результаты в
диапозоне от 100 до 2300, но снижение скорость проходил не так быстро как у
первой функции, в общем до 10000 функция выполняла приемлемое кол-во (чуть больше 2-х секунд)
Оценить сложность довольно сложно, но могу предположить, что сложность будет сравнимо с 
показательной, т.е. О(а ** n), где а>1. Вывод сделал на основе графика, она напоминает
показательную функцию до 10000, что не плохо, т.к. данная функция
не знает границы простого числа.

3. Решето Эратосфена как и следовало ожидать показала лучший результат на
больших числах, но к сожалению для данного алгоритма требуется очень
большое диапозон памяти для хранения списка, пытался заменить бинарным массивом,
но результата не дал, т.к. сработало ограничение размера массива (масчимальное число integer)
К сожалению не смог оценить как можно расчитать верхнюю границу простого числа.
сложность данного метода О(n*log(log(n)))

Полученные результаты:

get_prime_number_v1|10|0.09010000000000268 
get_prime_number_v2|10|0.11950000000000155
get_prime_number_v3|10|112.40149999999998
get_prime_number_v1|100|16.5864
get_prime_number_v2|100|2.501300000000012
get_prime_number_v3|100|156.23600000000002
get_prime_number_v1|200|80.3357
get_prime_number_v2|200|6.442300000000012
get_prime_number_v3|200|149.06179999999998
get_prime_number_v1|300|174.4211
get_prime_number_v2|300|10.700400000000055
get_prime_number_v3|300|158.01389999999992
get_prime_number_v1|400|360.66319999999996
get_prime_number_v2|400|17.741599999999913
get_prime_number_v3|400|169.74409999999995
get_prime_number_v1|500|591.5027000000001
get_prime_number_v2|500|26.885000000000048
get_prime_number_v3|500|215.75489999999985
get_prime_number_v1|600|1169.6209000000003
get_prime_number_v2|600|33.8712000000001
get_prime_number_v3|600|169.21539999999968
get_prime_number_v1|700|1260.9396999999997
get_prime_number_v2|700|41.22279999999989
get_prime_number_v3|700|158.4671000000002
get_prime_number_v1|800|1703.6108
get_prime_number_v2|800|44.78319999999947
get_prime_number_v3|800|154.99509999999984
get_prime_number_v1|900|2052.5298000000003
get_prime_number_v2|900|52.46110000000037
get_prime_number_v3|900|170.00049999999868
get_prime_number_v1|1000|2621.268299999999
get_prime_number_v2|1000|61.571600000000615
get_prime_number_v3|1000|189.5907000000001
get_prime_number_v1|1100|3261.7785000000003
get_prime_number_v2|1100|68.79539999999906
get_prime_number_v3|1100|191.5093999999993
get_prime_number_v1|1200|4829.260999999999
get_prime_number_v2|1200|71.04289999999835
get_prime_number_v3|1200|179.52539999999928
get_prime_number_v2|1300|83.49970000000084
get_prime_number_v3|1300|166.61579999999887
get_prime_number_v2|1400|93.0029999999995
get_prime_number_v3|1400|175.14229999999742
get_prime_number_v2|1500|99.59770000000034
get_prime_number_v3|1500|182.38929999999698
get_prime_number_v2|1600|117.32800000000054
get_prime_number_v3|1600|178.5533000000008
get_prime_number_v2|1700|117.72949999999938
get_prime_number_v3|1700|178.43179999999847
get_prime_number_v2|1800|123.74099999999899
get_prime_number_v3|1800|175.8316000000022
get_prime_number_v2|1900|136.46930000000168
get_prime_number_v3|1900|194.807100000002
get_prime_number_v2|2000|193.8555000000015
get_prime_number_v3|2000|220.74900000000142
get_prime_number_v2|2100|169.3794000000004
get_prime_number_v3|2100|191.2149999999997
get_prime_number_v2|2200|164.63899999999754
get_prime_number_v3|2200|185.1458000000008
get_prime_number_v2|2300|176.0023000000004
get_prime_number_v3|2300|190.54399999999916
get_prime_number_v2|2400|200.13289999999984
get_prime_number_v3|2400|186.02690000000166
get_prime_number_v2|2500|201.32549999999938
get_prime_number_v3|2500|176.20469999999955
get_prime_number_v2|2600|224.8222999999996
get_prime_number_v3|2600|187.46849999999782
get_prime_number_v2|2700|221.61239999999793
get_prime_number_v3|2700|175.38809999999927
get_prime_number_v2|2800|240.75360000000146
get_prime_number_v3|2800|182.95939999999788
get_prime_number_v2|2900|254.99300000000247
get_prime_number_v3|2900|198.1824000000003
get_prime_number_v2|3000|276.4635999999996
get_prime_number_v3|3000|190.17720000000082
get_prime_number_v2|3100|278.91429999999673
get_prime_number_v3|3100|182.57549999999867
get_prime_number_v2|3200|295.58549999999786
get_prime_number_v3|3200|207.27510000000038
get_prime_number_v2|3300|311.05750000000046
get_prime_number_v3|3300|184.1659
get_prime_number_v2|3400|305.70949999999897
get_prime_number_v3|3400|186.739799999998
get_prime_number_v2|3500|336.2913000000027
get_prime_number_v3|3500|184.85980000000168
get_prime_number_v2|3600|345.3575999999998
get_prime_number_v3|3600|195.2670999999988
get_prime_number_v2|3700|341.56850000000105
get_prime_number_v3|3700|185.29519999999877
get_prime_number_v2|3800|417.4013999999993
get_prime_number_v3|3800|194.2182999999993
get_prime_number_v2|3900|373.67240000000027
get_prime_number_v3|3900|179.5687000000008
get_prime_number_v2|4000|400.00659999999755
get_prime_number_v3|4000|258.468299999997
get_prime_number_v2|4100|518.9678999999999
get_prime_number_v3|4100|209.9982999999952
get_prime_number_v2|4200|549.9155999999984
get_prime_number_v3|4200|195.81660000000056
get_prime_number_v2|4300|437.3746000000054
get_prime_number_v3|4300|208.21400000000523
get_prime_number_v2|4400|477.74190000000516
get_prime_number_v3|4400|207.1240000000003
get_prime_number_v2|4500|505.5131000000017
get_prime_number_v3|4500|256.54660000000007
get_prime_number_v2|4600|545.2926999999975
get_prime_number_v3|4600|189.79919999999595
get_prime_number_v2|4700|513.3034999999993
get_prime_number_v3|4700|216.45149999999802
get_prime_number_v2|4800|519.9799999999968
get_prime_number_v3|4800|193.01580000000484
get_prime_number_v2|4900|539.6246999999973
get_prime_number_v3|4900|219.73119999999824
get_prime_number_v2|5000|591.0327999999936
get_prime_number_v3|5000|192.7833000000021
get_prime_number_v2|5100|584.8818999999992
get_prime_number_v3|5100|203.42790000000122
get_prime_number_v2|5200|587.762099999999
get_prime_number_v3|5200|207.39149999999995
get_prime_number_v2|5300|610.1790999999963
get_prime_number_v3|5300|208.16519999999628
get_prime_number_v2|5400|671.3177999999971
get_prime_number_v3|5400|217.0708000000019
get_prime_number_v2|5500|640.8701999999948
get_prime_number_v3|5500|194.05140000000642
get_prime_number_v2|5600|728.2450000000011
get_prime_number_v3|5600|205.84560000000351
get_prime_number_v2|5700|677.4375000000034
get_prime_number_v3|5700|200.95589999999675
get_prime_number_v2|5800|720.058900000005
get_prime_number_v3|5800|195.37130000000502
get_prime_number_v2|5900|720.1195999999968
get_prime_number_v3|5900|197.0741000000018
get_prime_number_v2|6000|852.0682999999991
get_prime_number_v3|6000|203.3970000000025
get_prime_number_v2|6100|797.5752999999984
get_prime_number_v3|6100|207.354500000001
get_prime_number_v2|6200|788.9442000000031
get_prime_number_v3|6200|226.7093000000031
get_prime_number_v2|6300|848.3507999999986
get_prime_number_v3|6300|214.9554000000009
get_prime_number_v2|6400|802.4204000000026
get_prime_number_v3|6400|208.50760000000435
get_prime_number_v2|6500|862.5430999999963
get_prime_number_v3|6500|206.23479999999716
get_prime_number_v2|6600|848.638600000001
get_prime_number_v3|6600|216.6677999999962
get_prime_number_v2|6700|897.3457000000025
get_prime_number_v3|6700|221.04480000000137
get_prime_number_v2|6800|874.839999999999
get_prime_number_v3|6800|212.74439999999828
get_prime_number_v2|6900|982.5362999999995
get_prime_number_v3|6900|237.63879999999915
get_prime_number_v2|7000|989.7277000000031
get_prime_number_v3|7000|239.17399999999844
get_prime_number_v2|7100|964.0603000000069
get_prime_number_v3|7100|246.33929999999538
get_prime_number_v2|7200|1011.9925999999992
get_prime_number_v3|7200|216.81929999999738
get_prime_number_v2|7300|1112.4802000000002
get_prime_number_v3|7300|215.12160000000335
get_prime_number_v2|7400|1010.1355000000041
get_prime_number_v3|7400|225.3331000000003
get_prime_number_v2|7500|1028.6999000000064
get_prime_number_v3|7500|243.39809999999318
get_prime_number_v2|7600|1163.6735999999955
get_prime_number_v3|7600|218.3904000000041
get_prime_number_v2|7700|1075.8935000000065
get_prime_number_v3|7700|230.74870000000658
get_prime_number_v2|7800|1128.5132999999946
get_prime_number_v3|7800|248.00969999999722
get_prime_number_v2|7900|1177.541699999992
get_prime_number_v3|7900|231.25150000001327
get_prime_number_v2|8000|1133.5803000000055
get_prime_number_v3|8000|222.98739999999384
get_prime_number_v2|8100|1192.2978999999998
get_prime_number_v3|8100|226.38010000000008
get_prime_number_v2|8200|1304.7681000000039
get_prime_number_v3|8200|321.3518000000022
get_prime_number_v2|8300|1298.4251000000029
get_prime_number_v3|8300|226.35169999999505
get_prime_number_v2|8400|1248.771099999999
get_prime_number_v3|8400|251.5094999999974
get_prime_number_v2|8500|1285.9006999999992
get_prime_number_v3|8500|223.89799999999127
get_prime_number_v2|8600|1292.289800000006
get_prime_number_v3|8600|226.2845999999996
get_prime_number_v2|8700|1326.6176999999998
get_prime_number_v3|8700|232.84340000000725
get_prime_number_v2|8800|1316.1105000000077
get_prime_number_v3|8800|239.16560000000686
get_prime_number_v2|8900|1414.308300000002
get_prime_number_v3|8900|226.38409999998999
get_prime_number_v2|9000|1469.100400000002
get_prime_number_v3|9000|254.56420000000435
get_prime_number_v2|9100|1369.3120000000079
get_prime_number_v3|9100|244.79090000001236
get_prime_number_v2|9200|1493.4135000000026
get_prime_number_v3|9200|238.56089999999597
get_prime_number_v2|9300|1449.4002999999934
get_prime_number_v3|9300|338.17969999999775
get_prime_number_v2|9400|1446.2177999999994
get_prime_number_v3|9400|225.67490000000134
get_prime_number_v2|9500|1627.5638999999983
get_prime_number_v3|9500|228.51359999999943
get_prime_number_v2|9600|1489.1614000000004
get_prime_number_v3|9600|262.79549999999574
get_prime_number_v2|9700|1556.1529999999948
get_prime_number_v3|9700|235.24379999999212
get_prime_number_v2|9800|1577.4123000000059
get_prime_number_v3|9800|241.87009999999987
get_prime_number_v2|9900|1618.273599999995
get_prime_number_v3|9900|231.89700000000357
get_prime_number_v2|10000|1576.8060999999989
get_prime_number_v3|10000|251.4828000000051
'''
