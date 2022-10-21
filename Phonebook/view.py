def print_phone_dict(aDict):
    for ind, el in aDict.items():
        print(ind, '\t\t', ('\t\t'.join(el)))
        # print(tabulate(aDict.items(), headers=['id', 'Name', 'LastName', 'Phone',], tablefmt="grid"))
        # print("{:<10s}{:<10s}".format("file1.txt", "file2.txt"))
        # print(tabulate(d.items(), headers=['NAME', 'VALUE'], tablefmt="grid"))


def input_entry(aDict):
    n = input('Введите Имя: ')
    ln = input('Введите Фамилию: ')
    ph = input('Введите Номер телефона: ')
    aDict[str(len(aDict))] = n, ln, ph
    return aDict


def del_entry(aDict : dict, num_id: int):
    print(aDict)  # Если комментирую, то перестаёт находить индекс??(((
    num_id = int(input('Для удаления введите id записи: '))
    while True:
        try:
            if num_id in aDict.keys():
                aDict[num_id] = '', '', ''
                return aDict
            else:
                num_id = input('id с таким номером нет. Попробуйте снова: ')      
                continue
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
