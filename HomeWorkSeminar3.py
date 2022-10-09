import random
from my_functions import *  # fillListRandom, getSumOdds

# Дополнительные функции определены в my_functions.py

# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, кторая найдёт сумму элементов списка, стоящих на нечётной позициях (не индексах).
# Пример: in >> 4, out [7,9,2,3] -> 9; in >> 5, out >> [2,5,2,7,9] -> 13

def task1():
    num = inputIntDigit('Задача 1. Введите длину списка: ')
    my_list = []
    my_sum = 0
    my_list = fillListRandom(my_list, num, 0, 10)
    print('Исходный список:', my_list)
    my_sum = getSumOdds(my_list, my_sum)
    print('Сумма элементов на нечётных позициях (не индексах):', my_sum)


# Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def task2():

    num = inputIntDigit('Задача 2. Введите длину списка: ')
    my_list = []
    mult_list = []
    middle = num//2
    my_list = fillListRandom(my_list, num, 0, 10)
    print('Исходный список:', my_list)

    if num % 2 != 0:
        middle += 1

    for i in range(middle):
        mult_list.append(my_list[i] * my_list[num - i - 1])

    print('Произведение пар чисел списка:', mult_list)

# From Seminar
# from random import randrange
#     result_list = [l_value*r_value for l_value, r_value in zip(left_side, right_side)]

#     my_list = [2, 3, 4, 5, 6]
#     res_list = []
#     for i in range(len(my_list)//2):
#         res_list.append(my_list[i]*my_list[-i-1])
#     if len(my_list)%2 != 0:
#         res_list.append(my_list[len(my_list)//2] ** 2)
#     print(res_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def task3():
    num = inputIntDigit('Задача 3. Введите длину списка: ')
    my_list = []
    float_list = []
    for _ in range(num):
        my_list.append(round(random.uniform(1, 10), 2))
    my_list[num-2] = 5  # Вставка числа, как в примере
    print('Исходный список: ', my_list)

    for i in range(num):
        a = round(my_list[i] % 1, 2)
        if a != 0:
            float_list.append(a)
    print('Преобразованный список: ', float_list)
    print('Pазница между макс. и мин. равна ',
          round((max(float_list) - min(float_list)), 2))


# From Seminar
# from random import uniform, randrange
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [round(val%1, 2) for val in my_list if isinstance(val, float)]
# print(new_list)
# print(max(new_list) - min(new_list))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101; 3 -> 11; 2 -> 10

def task4():
    num = inputIntDigit('Задача 4. Введите число в десятичном формате: ')
    print(f'Число {num} в двоичном формате будет: {bin(num)[2:]}')


# From Seminar
# from tokenize import Octnumber
# def int_input(message):
#     str1 = input(message)
#     if str1.isdigit():
#         result = int(str1)
#     else:
#         print('Введено не число')
#         result = -1
#     return result
# res_dec = int_input('Введите число: ')
# print(f'{res_dec} => {bin(res_dec)[2:]}')
# print(f'{res_dec} => {bin(res_dec)}')
# print(f'{res_dec} => {oct(res_dec)}')
# print(f'{res_dec} => {hex(res_dec)}')


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def task5():
    num = inputIntDigit('Задача 5. Введите число: ')
    fibo_list = []
    for i in range(num):
        fibo_list.append(fibonacci_pos(i))
        fibo_list.insert(0, fibonacci_neg(i))
    fibo_list.insert(0, fibonacci_neg(num))
    print(fibo_list)


task1()
task2()
task3()
task4()
task5()


# # [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# num = 8
# my_list = [1, 0, 1]
# for _ in range(1, num):
#     print(my_list[0], my_list[1] - my_list[0] )
#     print(my_list[-1], my_list[-2] + my_list[-1])
#     my_list.append(my_list[-2] + my_list[-1])
#     my_list.insert(0, my_list[1] - my_list[0])

# def pow(n, mult):
#     """
#     Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая 
#     перемножается с mult, а n – положительное целое
#     """
#     I = [[1, 0], [0, 1]]
#     x = [[1, 1], [1, 0]]
#     if n == 0:
#         print('Возвращается I, равна:', I)
#         return I
#     elif n == 1:
#         print('Возвращается Х, равен:', x)
#         return x
#     else:
#         print('n // 2, mult:', n // 2, I, mult)
#         y = pow(n // 2, mult)
#         print('y = mult(y, y), y =', y)
#         y = mult(y, y)
#         if n % 2:
#             print('y = mult(x, y), x, y =', x, y)
#             y = mult(x, y)
#         print('Возвращается y =', y)
#         return y

# def matrix_multiply(A, B):
#     BT = list(zip(*B))
#     print('BT', BT)
#     res= [[sum(a * b
#                  for a, b in zip(row_a, col_b))
#             for col_b in BT]
#             for row_a in A]
#     print('matrix_multiply=',res)
#     return res

# print(pow(8, matrix_multiply)[0][1])