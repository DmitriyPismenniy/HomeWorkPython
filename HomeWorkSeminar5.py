from curses.ascii import isdigit
from itertools import count
from queue import Empty
import random
from os import remove
from re import X


# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def task1():
    text = 'Съешь ещёабв этих мягабвких французских булок абв'
    # Вариант 1
    my_list = [elem for elem in text.split() if 'абв' not in elem]
    print(' '.join(my_list))
    # Вариант 2
    my_list = list(filter(lambda x: 'абв' not in x, text.split()))
    print(' '.join(my_list))

# 2. Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
#     ход друг после друга. Первый ход определяется жеребьёвкой. За один
#     ход можно забрать не более чем 28 конфет. Все конфеты оппонента
#     достаются сделавшему последний ход. Сколько конфет нужно взять
#     первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота - сделано сразу b)
#     b) Подумайте как наделить бота "интеллектом"


def input_check(n, message):
    while True:
        try:
            n = int(input(message))
            if 1 <= n <= 28:
                return n
            else:
                print("Вы ввели не верное число. Попробуйте снова: ")
                continue
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")


def input_bot(cand_bot, num_bot):
    a = (cand_bot - int(cand_bot / 29) * 29)
    if cand_bot <= 28:
        num_bot = cand_bot
    elif a < 28 and a != 0:
        num_bot = a
    else:
        num_bot = random.randint(1, 28)
    return num_bot


def amount_check(cand_ch, num_ch, plr_ch):
    cand_ch -= num_ch
    if cand_ch > 0:
        return (cand_ch)
    elif cand_ch == 0:
        print(f'Игрок {plr_ch} выиграл, Поздравляем!')
        exit()
    elif cand_ch < 0:
        cand_ch += num_ch
        while (cand_ch-num_ch) != 0:
            try:
                num_ch = int(
                    input("На столе нет столько конфет. Введите правильное число: "))
            except ValueError:
                print("Вы ввели не число. Попробуйте снова: ")
        print(f'Игрок {plr_ch} выиграл, Поздравляем!')
        exit()


def game_with_player(cand, plr1, plr2):
    number = 0
    while cand > 0:
        num1 = input_check(
            number, f'Игрок {plr1} возьмите конфеты в кол-ве от 1 до 28: ')
        cand = amount_check(cand, num1, plr1)
        print()
        print(f'На столе осталось {cand} конфет')
        num2 = input_check(
            number, f'Игрок {plr2} возьмите конфеты в кол-ве от 1 до 28: ')
        cand = amount_check(cand, num2, plr2)
        print()
        print(f'На столе осталось {cand} конфет')


def game_with_bot(cand, plr1, plr2):
    number = 0
    if plr1 == 'BOT':
        while cand > 1:
            num1 = input_bot(cand, number)
            print(f'Игрок BOT взял {num1} конфет: ')
            cand = amount_check(cand, num1, plr1)
            print()
            print(f'На столе осталось {cand} конфет')

            num2 = input_check(
                number, f'Игрок {plr2} возьмите конфеты в кол-ве от 1 до 28: ')
            cand = amount_check(cand, num2, plr2)
            print()
            print(f'На столе осталось {cand} конфет')
    else:
        while cand > 1:
            num1 = input_check(
                number, f'Игрок {plr1} возьмите конфеты в кол-ве от 1 до 28: ')
            cand = amount_check(cand, num1, plr1)
            print()
            print(f'На столе осталось {cand} конфет')

            num2 = input_bot(cand, number)
            print(f'Игрок BOT взял {num2} конфет: ')
            cand = amount_check(cand, num2, plr2)
            print()
            print(f'На столе осталось {cand} конфет')


def task2():
    candies = 81  # По условию 2021
    name_player1 = input('Первый игрок, введите своё имя: ')
    game = input('Вы хотите играть с ботом? Y(y) - Да или Any - Нет: ')
    if game == 'Y' or game == 'y':
        name_player2 = 'BOT'
    else:
        name_player2 = input('Второй игрок, введите своё имя: ')
    print()

    print('Жеребьёвка...')
    lot = random.randint(1, 11)
    if lot % 2:
        player1, player2 = name_player1, name_player2
    else:
        player1, player2 = name_player2, name_player1
    print('Согласно жеребьёвки, первый ход делает игрок: ', player1)
    print()

    print(f'Начало игры. На столе лежит {candies} конфет')
    if name_player2 == 'BOT':
        game_with_bot(candies, player1, player2)
    else:
        game_with_player(candies, player1, player2)


# 3. Создайте программу для игры в "Крестики-нолики".

def print_game(req_ch, game_dict_prt):
    req_ch = 0
    a1, b1, c1 = game_dict_prt['a1'], game_dict_prt['b1'], game_dict_prt['c1']
    a2, b2, c2 = game_dict_prt['a2'], game_dict_prt['b2'], game_dict_prt['c2']
    a3, b3, c3 = game_dict_prt['a3'], game_dict_prt['b3'], game_dict_prt['c3']

    print(f'     a      b      c')
    print(f'1    {a1}\t|   {b1}\t|  {c1}')
    print(f'   -----+-------+-----')
    print(f'2    {a2}\t|   {b2}\t|  {c2}')
    print(f'   -----+-------+-----')
    print(f'3    {a3}\t|   {b3}\t|  {c3}')

    if (a1 == a2 == a3 != '' or b1 == b2 == b3 != '' or c1 == c2 == c3 != ''
        or a1 == b1 == c1 != '' or a2 == b2 == c2 != '' or a3 == b3 == c3 != ''
            or a1 == b2 == c3 != '' or a3 == b2 == c1 != ''):
        req_ch = 1
        return req_ch


def ind_check(index_ch, dict_ch, message_ch):
    if '' in dict_ch.values():
        while True:
            try:
                index_ch = str(input(message_ch))
                if index_ch in dict_ch.keys():
                    if (dict_ch[index_ch]) == '':
                        return str(index_ch)
                    else:
                        print('Эта ячейка уже занята')
                else:
                    print('Ячейка вне диапазона поля')
            except ValueError:
                print("Вы ввели не число. Попробуйте снова: ")
    else:
        print('Ходов больше нет. Игра окончена')
        exit()


def task3():
    req = 0
    game_dict = \
        {'a1': '', 'b1': '', 'c1': '', 'a2': '', 'b2': '', 'c2': '',
            'a3': '', 'b3': '', 'c3': ''}
    print_game(req, game_dict)

    while True:
        ind_dict = ind_check(
            req, game_dict, 'Игрок 1 сделайте свой ход (x) в формате от a1 до с3: ')
        game_dict[ind_dict] = 'x'
        print_game(req, game_dict)
        if print_game(req, game_dict) == 1:
            print('Игрок 1, вы выиграли, поздравляем!')
            exit()

        ind_dict = ind_check(
            req, game_dict, 'Игрок 2 сделайте свой ход (o) в формате от a1 до с3: ')
        game_dict[ind_dict] = 'o'
        print_game(req, game_dict)
        if print_game(req, game_dict) == 1:
            print('Игрок 2, вы выиграли, поздравляем!')
            exit()


# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления
# данных. Входные и выходные данные хранятся в отдельных
# текстовых файлах. Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWW
# WWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 12W1B12W3B24W1B14W

def task4():
    # Сжатие
    data = open('./PythonHomeWork/Sem5InputFile.txt', 'r')
    strIn = str(data.readline())
    data.close
    print('strIn', strIn)

    my_count = 1
    out_list = []
    in_list = [_ for _ in strIn]
    # print('in1_list', in_list)

    for i in range(1, len(in_list)):
        if in_list[i] == in_list[i-1]:
            my_count += 1
        else:
            out_list.append(str(my_count))
            out_list.append(in_list[i-1])
            my_count = 1
    out_list.append(str(my_count))
    out_list.append(in_list[len(in_list)-1])
    # print('out_list', out_list)

    strOut = ''.join(out_list)
    print('strOut', strOut)
    with open('./PythonHomeWork/Sem5OutputFile.txt', 'w') as data:
        data.write(strOut)
    data.close

    # Восстановление
    strIn1 = ''
    in1_list = []
    i = 0
    while i < (len(strOut)):
        if strOut[i].isdigit():
            while strOut[i].isdigit():
                strIn1 += strOut[i]
                i += 1
            in1_list.append(int(strIn1))
            strIn1 = ''
        else:
            in1_list.append(strOut[i])
            i += 1
    # print('in1_list', in1_list)

    str2_Out = ''
    for i in range(0, len(in1_list), 2):
        str2_Out += in1_list[i] * in1_list[i+1]
    print('str2_Out', str2_Out)

    with open('./PythonHomeWork/Sem5Output2File.txt', 'w') as data:
        data.write(str2_Out)
    data.close


# task1()
# task2()
task3()
# task4()
