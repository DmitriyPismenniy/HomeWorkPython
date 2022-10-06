import random


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
