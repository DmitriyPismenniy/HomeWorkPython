from decimal import *
import math
from random import randint
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



task1()
task2()
task3()
task4()








# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.


# a = (str1_koef, str2_koef)

#     resultdict = {}

#     for dictionary in a:
#         for key in dictionary:
#             try:
#                 resultdict[key] += dictionary[key]
#             except KeyError:
#                 resultdict[key] = dictionary[key]

#     resultdict = dict(sorted(resultdict.items(), reverse=True))


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов
# f_1 = open('polynominal_1.txt','r')
# f_2 = open('polynominal_2.txt','r')
# x_1 = str(f_1.readline())
# x_2 = str(f_2.readline())
# def Power(x):
#     pow = []
#     for i in range(1, len(x)):
#         if x[i - 1] == '^':
#             pow.append(int(x[i]))
#     return pow
# def Koefficient(x, p):
#     koeff = str(x).replace(' = 0', '')
#     for i in range(p[0], 0, -1):
#         koeff = koeff.replace(f' * x^{i} + ', ' ')
#     koeff = [float(i) for i in koeff.split()]
#     return koeff
# pow_1 = Power(x_1)
# pow_2 = Power(x_2)
# koeff_1 = Koefficient(x_1, pow_1)
# koeff_2 = Koefficient(x_2, pow_2)
# pow_1.insert(len(pow_1), 0)
# pow_2.insert(len(pow_2), 0)
# p_matrix = [pow_1[0], pow_2[0]]
# polynominal_1 = {}
# for i in range(0, len(pow_1)):
#         polynominal_1[pow_1[i]] = koeff_1[i]
# polynominal_2 = {}
# for i in range(0, len(pow_2)):
#     polynominal_2[pow_2[i]] = koeff_2[i]
# polynominal_sum = {}
# for i in range(max(p_matrix), -1, -1):
#     if i in pow_1 and i not in pow_2:
#         polynominal_sum[i] = polynominal_1[i]
#     elif i not in pow_1 and i in pow_2:
#         polynominal_sum[i] = polynominal_2[i]
#     elif i in pow_1 and i in pow_2:
#         polynominal_sum[i] = polynominal_1[i] + polynominal_2[i]
# final = open('polynominal_sum.txt','w')
# for k, v in polynominal_sum.items():
#     if k != 0:
#         final.write(f'{v} * x^{k} + ')
#     else:
#         final.write(f'{v} = 0')
# f_1.close()
# f_2.close()
# final.close()

# https://github.com/KarinaKazamanova/Python

# >>> from collections import Counter
# >>> a = Counter({'menu': 20, 'good': 15, 'happy': 10, 'bar': 5})
# >>> b = Counter({'menu': 1, 'good': 1, 'bar': 3})
# >>> a + b
# Counter({'menu': 21, 'good': 16, 'happy': 10, 'bar': 8})


# https://pythonru.com/biblioteki/sympy-v-python
# x = Symbol('x')
# y = Symbol('y')
# # x = -1.038
# # y = 3**0.5
# t = (2*x + 3*y)**2 - 3*x*(4/3*x+4*y)
# simplify(t)
# f = 4*x**4-65*x**2+16
# solve(f)
# print(f)





