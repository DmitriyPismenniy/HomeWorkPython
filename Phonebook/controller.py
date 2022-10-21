import view as v
import user_choice as ur
import store_dict as sd


phone_dict = {}
phone_dict['id'] = 'Name', 'LastName', 'Phone'
num_del = ''


def click_button():
    print('\nДобро пожаловать в телефонный справочник!')
    sd.init_dict(phone_dict)   # Восстановление справочника из файла
    num_ch1 = ur.input_choice1()
    while num_ch1 != 0:
        if num_ch1 == 1:  # Вывод справочника
            v.print_phone_dict(phone_dict)
            num_ch1 = ur.input_choice1()

        elif num_ch1 == 2:  # Редактирование справочника
            num_ch2 = ur.input_choice2()
            while num_ch2 != 0:
                if num_ch2 == 1:  # Добавление записи
                    v.input_entry(phone_dict)
                    sd.save_phone(phone_dict)
                    num_ch2 = ur.input_choice2()
                elif num_ch2 == 2:  # Удаление записи
                    v.del_entry(phone_dict, num_del)
                    sd.save_phone(phone_dict)
                    num_ch2 = ur.input_choice2()
                elif num_ch2 == 3:  # Очистка справочника
                    print('Dell')  # Ещё не готово
                    num_ch2 = ur.input_choice2()
            else:
                num_ch1 = ur.input_choice1()

        elif num_ch1 == 3:  # Поиск в справочнике
            print('Искать')  # Ещё не готово
            num_ch1 = ur.input_choice1()
        else:  # Экспорт справочника
            print('Экспортировать')  # Ещё не готово
            num_ch1 = ur.input_choice1()
    print('\nСпасибо за использование телефонного справочника\n \
        До новых встреч!')