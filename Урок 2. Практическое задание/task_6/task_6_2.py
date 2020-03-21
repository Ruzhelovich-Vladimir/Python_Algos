"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randint


def guess(msg="", number=None, count=10):
    """
    Угадай число
    :param msg: Сообщение пользолателя
    :param number: Загаданное число
    :return:
    """
    if number is None:
        return "Ошибка.Число не загадано"
    user_number = int(input(msg))

    if user_number == number:
        return "Вы угадали!!!"
    if user_number > number:
        msg = "Вы ввели большое число. Попробуйте еще: "
    else:
        msg = "Вы ввели маленькое число. Попробуйте еще: "
    count -= 1
    if count < 1:
        return f"Вы не отгадали число: {number}"

    return guess(msg, number, count)


if __name__ == "__main__":

    print("ИГРА УГАДАЙ ЧИСЛО")
    NUMBER = randint(0, 100)
    print(guess("Угадай число от 0 до 100:", NUMBER))
