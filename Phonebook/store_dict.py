def init_dict(aDict: dict):
    data = open('./PythonHomeWork/Phonebook/phonebook.txt', 'r')
    pos = 0
    for line in data:
        my_list = [elem for elem in line.split(
            "'") if '(' not in elem and ', ' not in elem and '))\n' not in elem]
        if my_list[0] == 'id':
            aDict[my_list[0]] = my_list[1], my_list[2], my_list[3]
        else:
            if my_list[1] == my_list[2] == my_list[3] == '':
                pos += 1
            else:
                aDict[int(my_list[0]) - pos] = my_list[1], my_list[2], my_list[3]
    with open('./PythonHomeWork/Phonebook/phonebook.txt', 'w') as data:
        for ind, el in aDict.items():
            data.write((f'{str(ind), el}\n'))
    data.close            
    return aDict


def save_phone(aDict: dict):
    with open('./PythonHomeWork/Phonebook/phonebook.txt', 'w') as data:
        for ind, el in aDict.items():
            data.write((f'{str(ind), el}\n'))
    data.close
