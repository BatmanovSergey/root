from os import path
import csv 
from logger import logging
from prettytable import PrettyTable

def read_file(file):
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as t_file:
            csv.reader(t_file)
            all_person = []
            for row in t_file:   
                str_person = "".join(row)
                list_pers = str_person.strip().split(',')
                all_person.append(list_pers)
        return all_person
    else:
        print("The files do not exist in the system!")

c = read_file('Team.csv')
print(c)

def get_table(file): 
    list_all_person=read_file(file) 
    t = PrettyTable(list_all_person[0])
    for i in range(1, len(list_all_person)):
        t.add_row(list_all_person[i])
    print('Информация по всем сотрудникам')
    print(t)

get_table('Team.csv') 