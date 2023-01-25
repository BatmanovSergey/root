from os import path
from prettytable import PrettyTable
from tabulate import tabulate
import check_in

def read_and_get_dict(file_name: str)-> dict: # метод создания словаря из файла
    if path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as my_file:
            my_dict = {}
            for n, line in enumerate(my_file):
                line = line.rstrip().split(", ")
                my_dict.setdefault(n, [])
                my_dict[n] += line
            print(my_dict)         
    else:
        print("The files do not exist in the system!")

# read_and_get_dict('drivers.csv')

def read_all_file(file_name: str)-> str: # Метод чтения всего файла
    if path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as my_file:
            text = my_file.read()
            print(text)
        return text
    else:
        print("The files do not exist in the system!")

# read_all_file('drivers.csv')

def read_get_table(file_name: str): # метод вывода таблицы всего файла
    if path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as my_file:
            text = my_file.readline().strip('\ufeff\n').split(', ')
            t = PrettyTable(text)
            for n, line in enumerate(my_file):
                 line = line.strip().split(', ')
                 t.add_row(line)
            print('Информация по всем сотрудникам')
            print(t)
    else:
        print("The files do not exist in the system!")

# read_get_table('drivers.csv')

def add_in_file(file_name: str): # метод добавления нового сотрудника в файл
    if path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as my_file:
            my_dict = {}
            for n, line in enumerate(my_file):
                line = line.rstrip().split(", ")
                my_dict.setdefault(n, [])
                my_dict[n] += line
            # print(my_dict)
            last_id = sorted(my_dict.keys())[-1]
            lastname = check_in.check_name()
            bus = check_in.check_bus()
            route = check_in.check_route()
            new_last_id = last_id+1
            my_dict.setdefault(new_last_id, [])
            new_list = [str(new_last_id), lastname, bus, route]
            my_dict[new_last_id]+=new_list
            # print(my_dict)
        with open(file_name, "w", encoding="utf-8") as my_file:
            for value in my_dict.values():
                value = ", ".join(value)
                print(value)
                my_file.writelines(f'{value}\n')
            print(f'Новый сотрудник {lastname} добавлен в базу данных')
    else:
        print("The files do not exist in the system!")

# add_in_file('drivers.csv')

def delete_from_file(file_name: str):
     if path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as my_file:
            my_dict = {}
            for n, line in enumerate(my_file):
                line = line.rstrip().split(", ")
                my_dict.setdefault(n, [])
                my_dict[n] += line
            id_num = check_in.check_id()
            if id_num in my_dict:
                my_dict.pop(id_num)
            print(my_dict)

                
delete_from_file('drivers.csv')
        

        



