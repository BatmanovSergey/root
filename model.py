from os import path
import csv 
from logger import logging
from prettytable import PrettyTable

# дозапись  
def write_file(file, data):
        with open(file, 'a', encoding='utf-8') as t_file:  
            file_writer = csv.writer(t_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(data)


# перезапись 
def write_file_w(file, data):
    with open(file, 'w', encoding='utf-8') as t_file:  
        file_writer = csv.writer(t_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(data)
 
# чтение
def read_file(file):
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as t_file:
            csv.reader(t_file)#, delimiter=',')   
            # line_count = 0   
            all_person = []
            for row in t_file:   
                # line_count == 0
                str_person = "".join(row)
                list_pers = str_person.strip().split(',')
                all_person.append(list_pers)
                # line_count += 1   
            # else:
            #     str_person = "".join(row)
            #     list_pers = str_person.strip('\n').split(',')
            #     all_person.append(list_pers)
            #     line_count += 1          
        return all_person
    else:
        print("The files do not exist in the system!")

# метод вывода таблицы всех сотрудников
def get_table(file): 
    list_all_person=read_file(file) 
    t = PrettyTable(list_all_person[0])
    for i in range(1, len(list_all_person)):
        t.add_row(list_all_person[i])
    # print('Информация по всем сотрудникам')
    print(t)

# поиск
def find_info(file, data):
    find_list = []
    list_all_person = read_file(file)
    for i in range(1, len(list_all_person)):
        for j in range(len(list_all_person[i])):
            if list_all_person[i][j] == data:
                find_list.append(list_all_person[i])
            else: pass
    for k in range(len(find_list)+1):
        if k == 0:
            write_file_w('Find_info.csv', list_all_person[k])
        else:
            write_file('Find_info.csv', find_list[k-1])  
    print('Информация по вашему запросу.')                
    get_table('Find_info.csv')


# дозапись
def add_text(file):
    list_all_person = read_file(file)
    id = len(list_all_person)
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    post = input('Введите должность: ')
    while True:
        try:
            year_of_birth = int(input('Введите новый год рождения: '))
            new_person = [id, first_name, last_name, post, year_of_birth]
            break
        except Exception as e:
            print('Error: Для ввода используйте числа.')
    write_file(file, new_person)
    print('Данные успешно добавлены!')
    print('Обновлённый список команды корабля "ПЕРШЕРОН"')
    get_table('Team.csv')

# замена
def change_info(file, m_id, op):
    list_all_person = read_file(file)
    for i in range(1,len(list_all_person)-1):
        if list_all_person[i][0] == str(m_id):
            if op == 1:
                list_all_person[i][1] = input('Введите новую фамилию: ')
            elif op == 2:
                list_all_person[i][2] = input('Введите новое имя: ')
            elif op == 3:
                list_all_person[i][3] = input('Введите новую должность: ')
            elif op == 4:
                while True:
                    try:
                        year_of_birth = int(input('Введите новый год рождения: '))
                        list_all_person[i][4] = year_of_birth
                        break
                    except Exception as e:
                        print('Error: Для ввода используйте числа.')                       
            elif op == 5:
                list_all_person[i][1] = input('Введите новую фамилию: ')
                list_all_person[i][2] = input('Введите новое имя: ')
                list_all_person[i][3] = input('Введите новую должность: ')
                year_of_birth = input('Введите новый год рождения: ')
                while True:
                    try:
                        year_of_birth = int(input('Введите новый год рождения: '))
                        list_all_person[i][4] = year_of_birth
                        break
                    except Exception as e:
                        print('Error: Для ввода используйте числа.')
    for j in range(len(list_all_person)):
        if j == 0:
            write_file_w(file, list_all_person[j])
        else:
            write_file(file, list_all_person[j])
    print('Данные успешно изменены!')
    print('Обновлённый список команды корабля "ПЕРШЕРОН"')
    get_table('Team.csv') 


# удаление
def delete_info(file, m_id):
    list_all_person = read_file(file)
    print(list_all_person)
    for i in range(1,len(list_all_person)-1):
        if list_all_person[i][0] == str(m_id):
            list_all_person.pop(i)
            # for j in range(i,len(list_all_person)):
            #     ind = int(list_all_person[j][0])
            #     ind -= 1
            #     list_all_person[j][0] = ind
    for j in range(len(list_all_person)):
        if j == 0:
            write_file_w(file, list_all_person[j])
        else:
            write_file(file, list_all_person[j])
    print('Данные успешно удалены!')        
    print('Обновлённый список команды корабля "ПЕРШЕРОН"')        
    get_table('Team.csv')
