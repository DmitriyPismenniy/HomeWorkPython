# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример: 6782 -> 23; 0,56 -> 11

import random as r
from logging.config import dictConfig
from curses.ascii import isdigit
#from random import random


def task14():
    num = input('Введите вещественное число: ')
    my_sum = 0
    for i in range(len(num)):
        if num[i].isdigit():
            my_sum += int(num[i])
    print('Сумма цифр вещественного числа = ', my_sum)

# From seminar
# n = input("Введите число = ").replace('.', '').replace('-', '')
# while not n.isdigit():
#     n = input("Введите число = ").replace('.', '').replace('-', '')
# my_sum = 0
# n = list(n)
# print(map(int,n))
# my_sum = sum(list(map(int,n)))
# print(my_sum)


# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def task15():
    num = int(input('Введите число N: '))
    my_list = []
    result = 1
    for i in range(1, num+1):
        my_list.append(result * i)
        result *= i
    print('При N =', num, 'набор произведений чисел от 1 до N будет', my_list)

# Задайте список из n чисел последовательности (1+1/n)^n и выведите
# на экран их сумму.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def task16():
    num = int(input('Введите число N: '))
    my_dict = {i: round((1 + 1/i)**i, 2) for i in range(1, num+1)}
    print('Последовательность чисел будет:', dict(my_dict))
    print('А сумма элементов списка будет:', sum(dict.values(my_dict)))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число.

def task17():
    num = int(input('Введите число N: '))
    my_list = []
    for i in range(-num, num + 1):
        my_list.append(i)
    print(my_list)

    my_mult = 1
    path = 'file.txt'
    data = open(path, 'r')
    for line in data:
        if int(line) < len(my_list):
            my_mult *= my_list[int(line)]
        else:
            print('Выход за пределы диапазона')
            data.close
            exit()
    data.close
    print('Произведение элементов равно', my_mult)


# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random

def task18():
    num = int(input('Введите длину списка: '))
    my_list = []
    for i in range(num):
        my_list.append(r.randint(0, 10))
    print('Исходный список:', my_list)

    for i in range(num):
        j = r.randint(0, num-1)
        if i != j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
    print('Перемешанный список:', my_list)

# From Seminar
# import random
# my_list = [1, 2, 3, 4, 5, 6]
# for i, elem in enumerate(my_list):
#     a =  random.randint(0,len(my_list) -1)
#     if i != a:
#         elem,my_list[a] = my_list[a],elem
#         print(elem, my_list[a])
# print(my_list)

# From Seminar
# basic_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Исходный массив:\n {basic_array}')
# random_array = []
# for i in range(len(basic_array)):
#     random_array.append(basic_array.pop(random.randint(0, len(basic_array)-1)))
# print(f'Перемешанный массив:\n {random_array}')

# From Seminar
# my_list = [56, 89, 56, 34, 9, 6]
# new_list =  []
# for _ in (range(len(my_list))):
#     elem = my_list.pop(0)
#     new_list.append(elem)
# print(new_list)


task14()
task15()
task16()
task17()
task18()
