import random


def inputIntDigit(message):
    while True:
        try:
            n = int(input(message))
            return n
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")


def fillListRandom(aList, number, start_num, finish_num):
    aList = []
    for _ in range(number):
        aList.append(random.randint(int(start_num), int(finish_num)))
    return aList


def getSumOdds(aList, summa):
    summa = 0
    for i in range(0, len(aList), 2):
        summa += aList[i]
    return summa


def fibonacci_pos(n):
    if n in (0, 1):
        return 1
    return fibonacci_pos(n - 1) + fibonacci_pos(n - 2)


def fibonacci_neg(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_neg(n - 2) - fibonacci_neg(n - 1)
