from cgitb import strong
from decimal import *
import math
from random import randint
from symbol import power
from typing import Iterable
from my_functions import *


# Задача 1. Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}
def task1():
    num = float(input('Задача 1. Введите вещественное число: '))
    d = float(
        input('Введите требуемую точность в формате 10^{-1} ≤ d ≤10^{-10}: '))
    accuracy = 0

    while d < 1:  # Расчет смещения для требуемой точности
        d *= 10
        accuracy += 1

    f = math.floor(num)  # Расчет смещения для целой части числа
    while f > 1:
        f /= 10
        accuracy += 1

    getcontext().prec = accuracy
    print(f'{Decimal(num)/Decimal(1)}')


# From Seminar
# number = float(input())
# count = int(input())
# print(f'{number:.{count}f}')



# Задача 2. Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

def task2():
    num = inputIntDigit('Задача 2. Введите натуральное число N: ')
    my_list = []
    index = 2
    while index * index <= num:
        while not num % index:  # == 0:
            my_list.append(index)
            num = num / index
        index += 1
    if num > 1:
        my_list.append(int(num))
    print(my_list)

# From Seminar
# import math
# NUM = 26
# def prime_factors(inp_num):
#     res_list = []
#     while inp_num % 2 == 0:
#         res_list.append(2)
#         inp_num = inp_num / 2
# # Каждое составное число имеет хотя бы один простой множитель,
# # меньший или равный квадратному корню.
#     for i in range(3, int(math.sqrt(inp_num)) + 1, 2):
#         while inp_num % i == 0:
#             res_list.append(i)
#             inp_num = inp_num / i
#     if inp_num > 2:
#         res_list.append(int(inp_num))
#     return res_list
# print(prime_factors(NUM))


# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

def task3():
    num = inputIntDigit('Задача 3. Введите длину списка: ')
    my_list = []
    my_list = fillListRandom(my_list, num, 0, 10)
    print('Исходный список: ', my_list)

    result_list = [elem for elem in my_list if my_list.count(elem) == 1]
    print('Список неповторяющихся элементов: ', result_list)


# Задача 4. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def task4():
    num = inputIntDigit('Задача 4. Введите натуральную степень k: ')
    my_list = list(random.randint(0, 100) for _ in range(num+1))
    str1 = ''
    for i in range(num, -1, -1):
        if my_list[i] != 0:
            if i > 1:
                str1 += f'{my_list[i]}*x^{i} + '
            elif i == 1:
                str1 += f'{my_list[i]}*x '
            elif i == 0:
                str1 += f'+ {my_list[i]} '                
    str1 += '= 0'
    print(str1)
    # with open('/home/sysadm/GEEK BRAINS/Python/PythonHomeWork/task4file.txt', 'w') as data:
    with open('./PythonHomeWork/task4file.txt', 'w') as data:
        data.write(str1)
    data.close


#From Seminar
# import random
# num = int(input("Введите натуральную степень k: "))
# def magit_to_file(num: int):
#     if num > 0:
#         num1 = random.randint(0,100)
#         str_1 = f"{num1}*x^{num}"
#         for i in reversed(range(2, num)):
#             num1 = random.randint(0,100)
#             if num1 != 0:
#                 str_1 += f" + {num1}*x^{i}"
#         num1 = random.randint(0,100)
#         if num1 != 0:
#             str_1 += f" + {num1}*x"
#         num1 = random.randint(0,100)
#         if num1 != 0:
#             print(f"{str_1} + {num1} = 0")
#         else:
#             print(f"{str_1} = 0")
# magit_to_file(num)



from collections import Counter


def power_polinom(x):
    powIn_list = list(x.split())
    powOut_list = []
    for i in powIn_list:
        if '*x^' in i:
            f = i[i.find('^') + 1:]
            powOut_list.append(int(f))
        elif '*x' in i:
            powOut_list.append(1)
        elif i.isdigit() and int(i) != 0:
            powOut_list.append(0)
    return powOut_list


def koef_polinom(x):
    koefIn_list = list(x.split())
    koefOut_list = []
    for i in koefIn_list:
        if '*x' in i:
            f = i[:i.find('*')]
            koefOut_list.append(int(f))
        elif i.isdigit() and int(i) != 0:
           koefOut_list.append(int(i))
    return koefOut_list


def task5():
    strIn1 = ''
    strIn2 = ''
    strOut = ''

    data = open('./PythonHomeWork/Sem4PolinomIn1.txt', 'r')
    strIn1 = str(data.readline())
    data.close

    data = open('./PythonHomeWork/Sem4PolinomIn2.txt', 'r')
    strIn2 = str(data.readline())
    data.close

    # print('strIn1 = ', strIn1)
    # print('strIn2 = ', strIn2)

    pow_list1 = power_polinom(strIn1)
    pow_list2 = power_polinom(strIn2)
    koef_list1 = koef_polinom(strIn1)
    koef_list2 = koef_polinom(strIn2)

    # print(str1)
    # print('pow_list1  = ', pow_list1)
    # print('koef_list1 = ', koef_list1)
    # print(str2)
    # print('pow_list2  = ', pow_list2)
    # print('koef_list2 = ', koef_list2)

    polinomIn_dict1 = dict(zip(pow_list1, koef_list1))
    polinomIn_dict2 = dict(zip(pow_list2, koef_list2))

    a = Counter(polinomIn_dict1)
    b = Counter(polinomIn_dict2)
    polinomOut_dict = dict(reversed(sorted((a + b).items())))

    # print('polinomIn_dict1', polinomIn_dict1)
    # print('polinomIn_dict2', polinomIn_dict2)
    # print('polinomOut_dict преобраз', polinomOut_dict)

    powOut_list = list(polinomOut_dict.keys())
    koefOut_list = list(polinomOut_dict.values())

    # print('powOut_list  ', powOut_list)
    # print('koefOut_list ', koefOut_list)

    for i in range(len(polinomOut_dict)):
        k = koefOut_list[i]
        p = powOut_list[i]
        if p > 1:
            strOut += f'{k}*x^{p} +'
        elif p == 1:
            strOut += f'{k}*x'
        elif p == 0:
            strOut += f'+ {k}'
    strOut += '= 0'

    # print('strOut = ', strOut)

    with open('./PythonHomeWork/Sem4PolinomOut.txt', 'w') as data:
        data.write(strOut)
    data.close





task1()
task2()
task3()
task4()
task5()