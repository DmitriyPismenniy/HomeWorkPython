def input_choice1():
    print('\n\tДля просмотра справочника введите цифру \t1\n \
    \tДля редактирования справочника введите цифру \t2\n \
    \tДля поиска в справочнике введите цифру \t\t3\n \
    \tДля экспорта справочника введите цифру \t\t4\n \
    \tДля выхода из справочника введите цифру \t0')
    while True:
        try:
            n = int(input('Введите действие со справочником: '))
            if 0 <= n <= 4:
                return n
            else:
                print("Вы ввели не верное число. Попробуйте снова: ")
                continue
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")


def input_choice2():
    print('\n\tДля ввода данных введите цифру \t\t1\n \
    \tДля удаления данных введите цифру \t2\n \
    \tДля полной очистки введите цифру \t3\n \
    \tДля выхода из редактора введите цифру \t0')
    while True:
        try:
            n = int(input('Введите действие с редактором: '))
            if 0 <= n <= 3:
                return n
            else:
                print("Вы ввели не верное число. Попробуйте снова: ")
                continue
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")